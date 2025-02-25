# Runtime 885ms
# Memory 13.4MB

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.append(0)
        