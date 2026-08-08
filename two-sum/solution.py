class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counts = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in counts:
                counts[nums[i]] = i
            else:
                return [counts[diff], i ]


        