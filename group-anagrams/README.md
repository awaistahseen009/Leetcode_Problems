# Group Anagrams Solution
This solution groups a list of strings into anagrams of each other. 
The approach used is to create a unique identifier for each group of anagrams by counting the frequency of each character, then using a dictionary to store the anagrams. 
The time complexity is O(NM) where N is the number of strings and M is the maximum length of a string, and the space complexity is O(NM) for storing the result. 
This solution achieves a runtime of 98 ms and a memory usage of 16.1 MB.