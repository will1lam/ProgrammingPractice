# This problem is pretty fun, it's asking to iterate through an array and determine if values are unique. The easiest way to do this is with a dictionary and compare stored numbers.

# Prompt: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Creating the empty dictionary to store numbers later.
        foundNums = {}
        # Iterate through every number in the list.
        for num in nums:
            # Checking if the number in the list matches any keys in my dictionary.
            if num in foundNums:
                return True
            # If the number hasn't been found yet, just store the number as a key and keep looking. The matching value is irrelevant.
            else:
                foundNums[num] = None
        # In the case that all values are unique.
        return False     
        
