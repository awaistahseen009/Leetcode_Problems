class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        heap = []
        output = []
        for num, count in counts.items():
            heapq.heappush(heap, (count , num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for count , num in heap:
            output.append(num)
        return output
