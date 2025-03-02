class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        counter = dict()

        for x in arr:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1

        keys = counter.values()
        setKeys = set(keys)

        return len(setKeys) == len(keys)