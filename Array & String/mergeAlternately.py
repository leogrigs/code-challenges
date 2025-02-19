
# Runtime 10ms
# Memory 12.65MB

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        minLen = len(word1) if len(word1) < len(word2) else len(word2)
        bigger = word1 if len(word1) > len(word2) else word2
        result = ''

        for i in range(minLen):
            result += word1[i]
            result += word2[i]

        rest = bigger[minLen:]

        return result + rest

        

        