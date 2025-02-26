# Runtime 0ms
# Memory 12.5MB

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        result = [0]
        i = 0
        higher = 0
        for g in gain:
            newH = result[i] + g
            result.append(newH)
            if newH > higher:
                higher = newH
            i += 1

        return higher