#https://leetcode.com/problems/roman-to-integer/description/
# This one might seem intimidating at first, but it's really linear when you take a step back. Since we are converting Roman Numerals to base ten decimal,
# we only need to be concerned with our current value's translation, which also depends on the previous value. This means that something like "I" will
# always increment 1, but placed before a "V", then we see it adjusting the "V"s increment from 5 to 3 to sum to 4 overall for "IV" == 4. Pretty fun overall.
# It looks like a lot of conditionals, but once you see the pattern it becomes very clear.

class Solution:
    def romanToInt(self, s: str) -> int:
        intTotal = 0
        for index, char in enumerate(s):
            if char == 'I':
                intTotal += 1
            elif char == 'V':
                # If 'I' was previous value,
                # add 3 (1 + 3 = 4), otherwise add 5.
                if (s[index - 1] == 'I'):
                    intTotal += 3
                else:
                    intTotal += 5
            elif char == 'X':
                if (s[index - 1] == 'I'):
                    intTotal += 8
                else:
                    intTotal += 10
            elif char == 'L':
                if (s[index - 1] == 'X'):
                    intTotal += 30
                else:
                    intTotal += 50
            elif char == 'C':
                if (s[index - 1] == 'X'):
                    intTotal += 80
                else:
                    intTotal += 100  
            elif char == 'D':
                if (s[index - 1] == 'C'):
                    intTotal += 300
                else:
                    intTotal += 500
            elif char == 'M':
                if (s[index - 1] == 'C'):
                    intTotal += 800
                else:
                    intTotal += 1000

        return intTotal
