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


