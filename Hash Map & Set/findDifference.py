# Runtime 601ms
# Memory 12.8MB

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        list1 = set([x for x in nums1 if x not in nums2])
        list2 = set([y for y in nums2 if y not in nums1])

        return [list(list1), list(list2)]