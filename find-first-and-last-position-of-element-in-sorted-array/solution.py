class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 :
            return [-1 , -1]
        output = []
        # # [5,7,7,8,8,10], 8 Linear O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target :
        #         output.append(i)
        # if len(output) == 1:
        #     output.append(output[0])
        # if len(output) == 0:
        #     return [-1 , -1]
        # return output
        def _find_indices(nums, target, find_first):
            left  = 0
            right = len(nums) - 1
            ans = -1
            while left <= right:
                middle = (left  + right) // 2
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    ans = middle
                    if find_first:
                        right = middle - 1
                    else:
                        left = middle + 1
            return ans

        start = _find_indices(nums , target , True)
        end = _find_indices(nums , target, False)
        output.extend([start, end])
        return output


            

        