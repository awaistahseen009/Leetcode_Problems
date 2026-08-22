# Position of Element in an Infinite Sorted Array

## Problem

Given a **sorted infinite array** and a target value, find the index of the target.

The important constraint is that we **cannot use `len()`** to determine the size of the array because, conceptually, the array is infinite.

### Example

```text
nums = [3, 4, 5, 6, 7, 8, 9, 10, ...]
target = 4

Output:
1
```

---

## Approach

The idea is to use a **window-based binary search**.

Since we do not know the size of the array, we start with a small search window.

For example, with:

```python
window_size = 5
```

the initial window is:

```text
left = 0
right = 5

[ 3, 4, 5, 6, 7, 8, ... ]
  ↑              ↑
 left           right
```

We then calculate the middle:

```python
middle = (left + right) // 2
```

and compare the target with:

```python
nums[middle]
```

### Target is greater than the middle value

If:

```python
target > nums[middle]
```

the target must be somewhere to the right.

Therefore:

```python
left = middle + 1
```

We also move the right boundary forward to expand the search window:

```python
right = middle + 1 + window_size
```

Conceptually:

```text
Current window:

[left ........ middle ........ right]

Target is greater
              ↓

               [middle + 1 ........ new right]
```

### Target is smaller than the middle value

If:

```python
target < nums[middle]
```

the target must be somewhere to the left.

Therefore:

```python
right = middle - 1
```

This reduces the current search context.

### Target is found

If:

```python
target == nums[middle]
```

we return:

```python
middle
```

because `middle` is the index of the target.

---

## Implementation

```python
def position_of_element(nums: list, target: int, window_size=5):
    """
    Find the position of an element in a sorted infinite array.

    Rules:
    - The array is considered infinite, so we cannot use len(nums).
    - We use a fixed-size window to progressively search the array.
    - Start with a window from index 0 to `window_size`.
    - Perform binary search inside the current window.
    - If the target is greater than the middle value:
        - Move `left` to `middle + 1`.
        - Shift the right boundary forward by `window_size`.
        - This expands the search toward the right.
    - If the target is smaller than the middle value:
        - Move `right` to `middle - 1`.
        - This reduces the current search context.
    - If the target is found, return its index.
    - If no matching element is found, return None.

    Args:
        nums (list): A sorted array of values. The array is treated
            conceptually as infinite, so its length is not used.
        target (int): The value whose index we want to find.
        window_size (int): The initial size of the search window and
            the amount by which the window expands.

    Returns:
        int | None: The index of `target` if it is found; otherwise None.
    """

    left = 0
    right = window_size

    while left <= right:
        middle = (left + right) // 2

        if target == nums[middle]:
            return middle

        elif target > nums[middle]:
            left = middle + 1
            right = middle + 1 + window_size

        elif target < nums[middle]:
            right = middle - 1

    print("No answer found")
    return None
```

---

## Complexity

The exact complexity depends on how the window is expanded.

For a target located at index `n`, the search needs to progressively move toward the target before performing the binary-search-style narrowing.

The important idea is that we avoid scanning the array linearly from index `0`.

The binary-search portion of the search operates in:

```text
O(log n)
```

time once the relevant search range has been established.

Space complexity is:

```text
O(1)
```

because only a few pointer variables are used.

---

## Key Learning

This problem is primarily testing how to handle **binary search when the boundaries of the array are unknown**.

The important distinction to understand is:

```text
Known-size array
        ↓
left = 0
right = len(nums) - 1
```

versus:

```text
Unknown / infinite array
        ↓
Start with a window
        ↓
Expand the window when necessary
        ↓
Search within the discovered range
```

The core variables are:

```python
left
right
middle
```

and the important comparison is always between the **target value** and the **value at the middle index**:

```python
target < nums[middle]
target > nums[middle]
target == nums[middle]
```
