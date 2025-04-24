# Two Sum

# The trick to two sum, is finding a second target, what I mean by this is you need to know the value of the current num subtracted from the given target. This integer
# will either already be in a dictionary you stored, or hasn't been found yet which means you need to store it in a dictionary. In the case that the second target is
# present, you can simply return it's index as well as your current num's index in an array, or store it and break out to return. Overall, a pretty classic problem,
# but I would recomend solving it in a brute force method first.

# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#          You may assume that each input would have exactly one solution, and you may not use the same element twice.
#          You can return the answer in any order.

# Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a dictionary to store values and indexes for later.
        foundNums = {}
        # Used for my indexes if I find two sum.
        solutionList = []
        for index, num in enumerate(nums):
            # Iterating through nums trying to see if I can find that second target.
            secondNum = target - num
            # In the case that I find it, just append it to the array and return it.
            if secondNum in foundNums:
                solutionList.append(foundNums[secondNum])
                solutionList.append(index)
            else:
                foundNums[num] = index
        return solutionList
