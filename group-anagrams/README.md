# Group Anagrams Solution
This solution groups a list of strings into anagrams of each other.
The approach used is to sort each string and compare the sorted strings for equality, grouping matching strings together.
### Time and Space Complexity
* Time complexity: O(NMlogM), where N is the number of strings and M is the maximum length of a string
* Space complexity: O(NM), for storing the sorted strings and output groups
Note: The provided implementation has a runtime of 2352 ms and uses 16.2 MB of memory.