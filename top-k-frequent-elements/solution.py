class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        sorted_counts = sorted(counts, key = lambda x: counts[x], reverse = True)
        output = []
        for idx in sorted_counts[:k]:
            output.append(idx)
        
        return output
