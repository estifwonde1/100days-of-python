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
