# Peak Index in a Mountain Array  

**Problem** – Find the index of the peak element in a mountain array (strictly increasing then strictly decreasing).  

**Solution Overview**  
Binary search exploits the monotonic property: if `arr[mid] < arr[mid+1]` the peak lies to the right, otherwise it lies at `mid` or left. Shrink the search interval until `left == right`, which is the peak index.  

**Complexity**  
- **Time:** O(log n) – each iteration halves the search space.  
- **Space:** O(1) – only a few integer variables are used.  

**Reference Implementation (Python 3)**  

```python
class Solution:
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```
