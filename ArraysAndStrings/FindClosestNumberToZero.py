# https://leetcode.com/problems/find-closest-number-to-zero/description/

# Pretty interesting how they worded it as "finding the closest number to zero", but this is basically asking for the minimum absolute value in a string.
# So that's exactly what were going to do, and there is one special case where we have the same absolute value, but we just choose the larger in that case.

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Treat the first index as the minumum.
        closestToZero = nums[0]
        for num in nums:
            # As we sort through the values, if the value is smaller than our current value, store the new value.
            if abs(num) < abs(closestToZero):
                closestToZero = num
            # This is the special case I mentioned earlier, where we would just take the larger value if their absolute values are the same.
            elif abs(num) == abs(closestToZero):
                if num > closestToZero:
                    closestToZero = num
        return closestToZero
