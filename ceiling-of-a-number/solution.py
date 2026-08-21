# Assume the array is sorted

"""
Bruteforce, Naive search O(n)
"""

def ceil_naive(nums:list, target:int):
    for num in nums:
        if num >= target:
            return num
        continue

"""
Can we improve it ? 
Yes by binary search and can try to make in O(logn)
"""

def ceil_num(nums:list, target:int):
    """
    Finds the ceiling of a target number in a sorted list.

    :param nums: List[int] - A sorted list of integers.
    :param target: int - The target number to find the ceiling for.
    :return: int or None - The index of the ceiling number if found, otherwise None.
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2 
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle +  1
        if nums[middle]  >target:
            right = middle

    if nums[right] < target:
        print("No ceil is being found")
        return None
    return right

if __name__== "__main__":
    nums = [2, 3, 5, 9, 16,17, 18,20, 25]
    target = 100
    # print(ceil_naive(nums, target))
    print(ceil_num(nums, target))
