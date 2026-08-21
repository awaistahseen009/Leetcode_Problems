# Floor of a Number

## Problem Description
Given a sorted list of integers, find the largest number in the list that is less than or equal to a given target number. If no such number exists, return `None`.

## Possible Solutions

### 1. Naive Approach (Brute Force)
- **Approach**: Iterate through the list, keeping track of the last number seen that is less than or equal to the target. Stop as soon as a number greater than the target is found (since the list is sorted, nothing further can be the floor).
- **Time Complexity**: O(n), where `n` is the size of the list.
- **Space Complexity**: O(1), as no additional space is used.

### 2. Optimized Approach (Binary Search)
- **Approach**: Use binary search to find the floor of the target in O(log n) time.
  - Start with two pointers, `left` and `right`, at the bounds of the list.
  - Calculate the middle index and compare the middle element with the target.
    - If `nums[middle] == target`, that index is the floor — return it directly.
    - If `nums[middle] > target`, the floor cannot be at or to the right of `middle`, so shrink the window: `right = middle - 1`.
    - If `nums[middle] < target`, `middle` is a valid candidate, but a larger valid candidate might exist to the right, so shrink the window: `left = middle + 1`.
  - When the loop ends (`left > right`), `right` holds the index of the last confirmed valid candidate (every step that moved `right` was in response to overshooting, so `right` naturally settles on the correct answer — `left`, by contrast, has stepped one past it).
  - After the loop, check whether `nums[right]` actually satisfies `nums[right] <= target`. If not, no floor exists in the array.
- **Time Complexity**: O(log n), as the search space is halved at each step.
- **Space Complexity**: O(1), as the search is performed in-place.

## Why `right` and not `left`?
This uses the classic `left <= right` / `left = middle + 1` / `right = middle - 1` binary search style. In this style:
- `left` only ever advances past positions confirmed **too small** — by the end it has stepped one index too far.
- `right` only ever retreats past positions confirmed **too large** — by the end it has landed exactly on the last valid (small-enough) candidate.

This is the mirror image of the ceiling problem, where `left` (not `right`) holds the correct answer at the end, because the roles of "too small" and "too large" are swapped.

## Example Usage
```python
nums = [2, 3, 5, 9, 16, 17, 18, 20, 25]
target = 8

# Naive approach
print(floor_naive(nums, target))  # Output: 5

# Optimized approach (returns index, not value)
print(floor_num(nums, target))  # Output: 2  (nums[2] == 5)
```

## Edge Cases to Test
- Target smaller than every element in the list → no floor exists, should return `None`.
- Target larger than every element in the list → floor is the last element.
- Target exactly equal to an element in the list → floor is that element itself.
- Single-element list, with target equal to, above, and below that element.