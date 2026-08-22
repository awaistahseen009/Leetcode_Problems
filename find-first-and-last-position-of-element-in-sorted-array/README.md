# Find First and Last Position of Element in Sorted Array  

## Problem  
Given a **sorted** integer array `nums` and an integer `target`, return the starting and ending indices of `target`. If `target` is absent, return `[-1, -1]`.  

## Solution Overview  
The algorithm performs two binary‑search passes:  

1. **Leftmost index** – search for `target` and, upon a match, continue left (`right = mid‑1`).  
2. **Rightmost index** – similar, but continue right (`left = mid+1`).  

A helper `_find_indices(nums, target, find_first)` encapsulates the logic, returning `-1` when the value is not found. The final result is `[leftmost, rightmost]`.  

## Complexity  
- **Time:** `O(log n)` (two binary searches)  
- **Space:** `O(1)` extra space  

## Usage  

```python
sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
```