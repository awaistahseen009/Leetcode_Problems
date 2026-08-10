class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        processed_indices = set()
        sorted_strs = []
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))

        for i in range(len(strs)):
            group = [strs[i]]
            if i in processed_indices:
                continue
            for j in range(i+1, len(strs)):
                if (sorted_strs[i] == sorted_strs[j]) and j not in processed_indices:
                    group.append(strs[j])
                    processed_indices.add(j)
            output.append(group)
        return output
