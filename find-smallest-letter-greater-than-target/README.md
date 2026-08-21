# LeetCode – Find Smallest Letter Greater Than Target  

**Problem**: Given a sorted list `letters` of lowercase English characters (with possible duplicates) and a target character `target`, return the smallest character in the list that is strictly greater than `target`. The list is circular, so if no such character exists, return the first element.  

**Approach**  
Binary search is used to locate the first index whose character exceeds `target`.  
- Maintain `left` and `right` pointers.  
- If `letters[mid]` ≤ `target`, move `left` to `mid + 1`; otherwise shrink `right` to `mid`.  
- After the loop, `right` points to the candidate. If it still ≤ `target`, the answer wraps around to `letters[0]`.  

**Complexity**  
- **Time**: O(log n) where *n* = `len(letters)`  
- **Space**: O(1) (in‑place pointers only)  

**Usage**  

```python
sol = Solution()
print(sol.nextGreatestLetter(["c","f","j"], "a"))  # → "c"
print(sol.nextGreatestLetter(["c","f","j"], "j"))  # → "c"
```