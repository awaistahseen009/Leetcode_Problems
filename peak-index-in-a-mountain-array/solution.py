class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1
        while left<right:
            middle = (left + right) // 2
            if arr[middle + 1] >= arr[middle]:
                left = middle + 1
            else:
                right = middle

        return right 

        