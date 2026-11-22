import numphy
import polar
import turtle
import pandas
import random
import datetime
import math
x
n 
while true:
    print("another streak extender")
def distinct_prime_factors(n: int) -> list[int]:
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors
def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop for total passes through the list
    for i in range(n):
        swapped = False
        
        # Inner loop for adjacent comparisons
        # The last 'i' elements are already sorted, so we can skip them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements in place using Python's tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no elements were swapped in this pass, the list is sorted
        if not swapped:
            break
            
    return arr

# Example Usage
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", nums)
    
    sorted_nums = bubble_sort(nums)
    print("Sorted list:  ", sorted_nums)

def insertion_sort(sorted):
    for i in range(0,len(sorted-1)):
        for j in range(1,len(sorted-1):
            if sorted[i] < sorted[j]:
               sorted[i] = sorted[i]
            elif sorted[i] > sorted[j]:
               sorted[i] = sorted[j]
            else:
                continue
    print(sorted)
sorted = [1,7,9,5,8]
insertion_sort(sorted)



some = randint(1,100)
gott= True
while gott:
    if some =! 0:
        print ("u need to sleep")
    else:
        gott = False

for i in range(some):
    m = i%2
    if m == 0:
        print (f"{m} is an even number")
    else:
        print(f"{m} that is odd i wonder why")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    def display(self):
        elements = []
        current = self.head
        while current:
            elemets.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base-10 digits (0-9)

    # Count occurrences of each digit at the current place value
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Convert counts to cumulative indices for stable placement
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array in reverse to preserve stability
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy sorted elements back into original list
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1  # Start at the 1s place (10^0)

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


# Example usage
nums = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(nums))
# Output: [2, 24, 45, 66, 75, 90, 170, 802]

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Case 1 & 2: Leaf node or single child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: Two children (replace with in-order successor)
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# Example Usage
bst = BinarySearchTree()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print(bst.inorder())   # Output: [20, 30, 40, 50, 60, 70, 80]
print(bst.search(40))  # Output: True
bst.delete(30)
print(bst.inorder())   # Output: [20, 40, 50, 60, 70, 80]
