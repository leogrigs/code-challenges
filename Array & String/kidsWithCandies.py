# Runtime: 0ms
# Memory: 12.56MB

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatestAmount = max(candies)
        result = []

        for candy in candies:
            result.append((candy + extraCandies) >= greatestAmount)

        return result
        