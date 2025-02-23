# Runtime 514ms
# Memory 13.4MB

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["a", "e", "i", "o", "u"]
        aux = []
        result = ""
        for c in s:
            if c.lower() in vowels:
                aux.append(c)

        for c in s:
            if c.lower() in vowels:
                newC = aux.pop()
                result += newC
            else:
                result += c

        return result
                

        