# Find Peak Element  

**Problem (one‑liner)**  
Given an integer array `nums`, return the index of any *peak* element—an element strictly greater than its neighbors.  

**Approach**  
Binary search is used to achieve O(log n) time.  
- Keep `left` and `right` pointers at the array bounds.  
- At each step examine `mid`. If `nums[mid]` is greater than both neighbors, it is a peak.  
- Otherwise, move the search window towards the larger neighbor: if `nums[mid] > nums[mid+1]` go left, else go right.  
The loop terminates when `left == right`, which must be a peak.  

**Complexity**  
- **Time:** O(log n)  
- **Space:** O(1) (in‑place pointers only)  

**Usage**  
```python
sol = Solution()
idx = sol.findPeakElement([1,2,3,1])   # returns 2
```