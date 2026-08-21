# Ceiling of a Number

## Problem Description
Given a sorted list of integers, find the smallest number in the list that is greater than or equal to a given target number. If no such number exists, return `None`.

## Possible Solutions

### 1. Naive Approach (Brute Force)
- **Approach**: Iterate through the list and return the first number that is greater than or equal to the target.
- **Time Complexity**: O(n), where `n` is the size of the list.
- **Space Complexity**: O(1), as no additional space is used.

### 2. Optimized Approach (Binary Search)
- **Approach**: Use binary search to find the ceiling of the target in O(log n) time. 
  - Start with two pointers, `left` and `right`, at the bounds of the list.
  - Calculate the middle index and compare the middle element with the target.
  - Adjust the search window based on the comparison until the ceiling is found or the search space is exhausted.
- **Time Complexity**: O(log n), as the search space is halved at each step.
- **Space Complexity**: O(1), as the search is performed in-place.

## Example Usage
```python
nums = [2, 3, 5, 9, 16, 17, 18, 20, 25]
target = 10

# Naive approach
print(ceil_naive(nums, target))  # Output: 16

# Optimized approach
print(ceil_num(nums, target))  # Output: 16