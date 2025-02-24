# Runtime 0ms
# Memory 12.7MB

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        score = 0
        for l in s:
            for i in range(j, len(t)):
                if l == t[i]:
                    j = i + 1
                    score += 1
                    break

        return score == len(s)
        