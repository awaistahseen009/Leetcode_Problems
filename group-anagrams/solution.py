class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        counts = {}
        def prepare_string(text):
                numbers = [ord(char) - 96 for char in text.lower() if char.isalpha()]
                z_numbers = [0 for _ in range(26)]
                for num in numbers:
                    z_numbers[num-1] += 1 
                return "".join([str(num)+"-" for num in z_numbers])

        for ana in strs:
            _id = prepare_string(ana)
            if _id not in counts:
                counts[_id] = [ana]
            else:
                counts[_id].append(ana)
        output = []
        for value in counts.values():
            output.append(value)
        
        return output