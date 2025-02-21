# Runtime: 93ms
# Memory: 18.67MB

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return nums[0]

        initial = nums[:k]
        avarage = sum(initial)
        result = avarage
        i = 1

        while i < len(nums) - k + 1:
            avarage = avarage + nums[i + k - 1] - nums[i-1]
            if avarage > result:
                result = avarage
            i+=1

        return result/float(k)
        