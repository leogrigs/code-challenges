# Runtime 0ms
# Memory 12.8MB

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        list1 = set(nums1)
        list2 = set(nums2)

        list1.difference_update(set(nums2))
        list2.difference_update(set(nums1))

        return [list(list1), list(list2)]

        