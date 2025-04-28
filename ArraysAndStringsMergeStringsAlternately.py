# https://leetcode.com/problems/merge-strings-alternately/
# This problem is not too bad, I would just just think about it as a zipper or traffic merging, just put one thing from each side. No need to overcomplicate.
# The three main steps are finding the sizes of the two strings, appending the equal sized part, then adding the extra portion if it exists.
# In the future I'll revisit this problem with "".join() and .extend() for efficiency. 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #two cases, either str1 or srt2 longer
        #for the shorter/equal case, find the length
        if (len(word1) > len(word2)):
            firstMergeSize = len(word2)
            secondMergeSize = len(word1) - len(word2)
        else:
            firstMergeSize = len(word1)
            secondMergeSize = len(word2) - len(word1)
        #then merge alternate
        mergedString = ""
        for i in range(firstMergeSize):
            mergedString += word1[i]
            mergedString += word2[i]
        #once counter runs out, append the longer onto the end of new string
        for i in range(firstMergeSize, firstMergeSize + secondMergeSize):
            if (len(word1) > len(word2)):
                mergedString += word1[i]
            else:
                mergedString += word2[i]
        return mergedString
        
