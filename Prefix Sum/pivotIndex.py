# Runtime 0ms
# Memory 13.5MB

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        leftSum = 0
        rightSum = sum(nums[1:])
        if leftSum == rightSum:
            return 0

        for i in range(1, len(nums)):
            leftSum += nums[i - 1]
            rightSum -= nums[i]

            if leftSum == rightSum:
                return i
        
        return -1


        
        