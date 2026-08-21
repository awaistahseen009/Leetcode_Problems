class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1 
        while left < right:
            middle = (left + right) // 2
            if (nums[middle] > nums[middle + 1]) and (nums[middle] > nums[middle - 1]):
                return middle
            else:
                if nums[middle] > nums[middle + 1]:
                    right = middle - 1 
                else:
                    left = middle + 1
        return left
        
                
        