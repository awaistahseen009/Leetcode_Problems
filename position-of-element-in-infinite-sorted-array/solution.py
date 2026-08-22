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

    Example:
        nums = [3, 4, 5, 6, 7, ...]
        target = 4

        position_of_element(nums, target)
        # Returns: 1
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


if __name__ == "__main__":
    nums = [(i + 2) + 1 for i in range(100)]
    target = 41

    print(position_of_element(nums, target))
