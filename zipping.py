def crc32(data: bytes) -> int:
    """1. Pure-Python CRC-32 Checksum (IEEE 802.3 polynomial)."""
    crc = 0xFFFFFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
    return crc ^ 0xFFFFFFFF


class BitWriter:
    """Helper to write individual bits (LSB-first, as required by DEFLATE)."""
    def __init__(self):
        self.bytes = bytearray()
        self.current_byte = 0
        self.bit_count = 0

    def write_bits(self, value: int, num_bits: int):
        for i in range(num_bits):
            bit = (value >> i) & 1
            self.current_byte |= (bit << self.bit_count)
            self.bit_count += 1
            if self.bit_count == 8:
                self.bytes.append(self.current_byte)
                self.current_byte = 0
                self.bit_count = 0

    def write_bits_msb(self, value: int, num_bits: int):
        """Huffman codes are written MSB-first into the LSB-first stream."""
        for i in range(num_bits - 1, -1, -1):
            bit = (value >> i) & 1
            self.write_bits(bit, 1)

    def flush(self) -> bytes:
        if self.bit_count > 0:
            self.bytes.append(self.current_byte)
        return bytes(self.bytes)


def lz77_compress(data: bytes, window_size: int = 256) -> list:
    """2. LZ77 Sliding Window: replaces repeated byte sequences with (length, distance)."""
    tokens = []
    i = 0
    n = len(data)
    while i < n:
        best_len = 0
        best_dist = 0
        start = max(0, i - window_size)
        # Search backward in window for longest match (min length 3)
        for j in range(start, i):
            length = 0
            while i + length < n and length < 10 and data[j + length] == data[i + length]:
                length += 1
            if length >= 3 and length > best_len:
                best_len = length
                best_dist = i - j
        if best_len >= 3:
            tokens.append(("MATCH", best_len, best_dist))
            i += best_len
        else:
            tokens.append(("LITERAL", data[i]))
            i += 1
    return tokens


def deflate_compress(data: bytes) -> bytes:
    """3. DEFLATE Stream: Encodes LZ77 tokens using RFC 1951 Fixed Huffman codes."""
    bw = BitWriter()
    # Block header: BFINAL=1 (last block), BTYPE=01 (Fixed Huffman) -> 3 bits: 1, 1, 0
    bw.write_bits(1, 1)
    bw.write_bits(1, 2)

    # RFC 1951 Length codes (lengths 3..10 map to codes 257..264 with 0 extra bits)
    # RFC 1951 Distance codes (simplified subset for common small distances)
    dist_table = [
        (1, 0, 0, 0), (2, 1, 0, 0), (3, 2, 0, 0), (4, 3, 0, 0),
        (5, 4, 1, 1), (7, 5, 1, 1), (9, 6, 2, 3), (13, 7, 2, 3),
        (17, 8, 3, 7), (25, 9, 3, 7), (33, 10, 4, 15), (49, 11, 4, 15),
        (65, 12, 5, 31), (97, 13, 5, 31), (129, 14, 6, 63), (193, 15, 6, 63)
    ]

    for token in lz77_compress(data):
        if token[0] == "LITERAL":
            lit = token[1]
            if lit <= 143:
                bw.write_bits_msb(0b00110000 + lit, 8)
            else:
                bw.write_bits_msb(0b110010000 + (lit - 144), 9)
        else:
            _, length, dist = token
            # Encode Length (3..10 -> 257..264 -> 7-bit Huffman code 0000001..0001000)
            len_code = 257 + (length - 3)
            bw.write_bits_msb(len_code - 256, 7)

            # Encode Distance (5-bit fixed Huffman code + extra bits)
            for base, code, extra_bits, mask in reversed(dist_table):
                if dist >= base:
                    bw.write_bits_msb(code, 5)
                    if extra_bits > 0:
                        bw.write_bits(dist - base, extra_bits)
                    break

    # End-of-Block symbol (256 -> 7 bits of 0)
    bw.write_bits_msb(0, 7)
    return bw.flush()


def u16(val: int) -> bytes:
    """Pack 16-bit unsigned integer as Little-Endian bytes."""
    return val.to_bytes(2, "little")


def u32(val: int) -> bytes:
    """Pack 32-bit unsigned integer as Little-Endian bytes."""
    return val.to_bytes(4, "little")


def create_zip(output_zip_path: str, input_files: dict[str, bytes]):
    """4. Assemble the PKZIP binary structure."""
    zip_body = bytearray()
    central_directory = bytearray()
    file_count = 0

    for filename, raw_data in input_files.items():
        name_bytes = filename.encode("utf-8")
        checksum = crc32(raw_data)
        compressed_data = deflate_compress(raw_data)
        local_header_offset = len(zip_body)

        # --- A. Local File Header (30 bytes + filename) ---
        local_header = (
            b"\x50\x4b\x03\x04"          # Local file header signature
            + u16(20)                    # Version needed to extract (2.0)
            + u16(0)                     # General purpose bit flag
            + u16(8)                     # Compression method (8 = DEFLATE)
            + u16(0) + u16(0)            # Last mod time & date
            + u32(checksum)              # CRC-32 of uncompressed data
            + u32(len(compressed_data))  # Compressed size
            + u32(len(raw_data))         # Uncompressed size
            + u16(len(name_bytes))       # File name length
            + u16(0)                     # Extra field length
            + name_bytes                 # File name
        )
        zip_body.extend(local_header)
        zip_body.extend(compressed_data)

        # --- B. Central Directory File Header (46 bytes + filename) ---
        cd_header = (
            b"\x50\x4b\x01\x02"          # Central directory signature
            + u16(20) + u16(20)          # Version made by & needed
            + u16(0)                     # General purpose bit flag
            + u16(8)                     # Compression method (8 = DEFLATE)
            + u16(0) + u16(0)            # Last mod time & date
            + u32(checksum)              # CRC-32
            + u32(len(compressed_data))  # Compressed size
            + u32(len(raw_data))         # Uncompressed size
            + u16(len(name_bytes))       # File name length
            + u16(0) + u16(0)            # Extra field & file comment lengths
            + u16(0) + u16(0)            # Disk number start & internal attrs
            + u32(0)                     # External file attributes
            + u32(local_header_offset)   # Relative offset of local header
            + name_bytes                 # File name
        )
        central_directory.extend(cd_header)
        file_count += 1

    cd_offset = len(zip_body)
    cd_size = len(central_directory)

    # --- C. End of Central Directory Record (22 bytes) ---
    eocd = (
        b"\x50\x4b\x05\x06"              # EOCD signature
        + u16(0) + u16(0)                # Disk numbers
        + u16(file_count)                # Entries on this disk
        + u16(file_count)                # Total entries
        + u32(cd_size)                   # Size of central directory
        + u32(cd_offset)                 # Offset of central directory
        + u16(0)                         # ZIP file comment length
    )

    with open(output_zip_path, "wb") as f:
        f.write(zip_body)
        f.write(central_directory)
        f.write(eocd)


# --- Example Usage ---
if __name__ == "__main__":
    sample_text = b"Hello world! Hello world! Building a ZIP file from scratch in Python! " * 5
    create_zip("scratch_output.zip", {"hello.txt": sample_text})
    print("Created scratch_output.zip successfully!")

