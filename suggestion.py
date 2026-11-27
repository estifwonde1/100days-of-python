class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Autocomplete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def suggest(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)

# Example usage
ac = Autocomplete()
for w in ["python", "pytorch", "pyramid", "pandas"]:
    ac.insert(w)

print(ac.suggest("py"))
# Output: ['python', 'pytorch', 'pyramid']
