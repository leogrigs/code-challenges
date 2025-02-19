# Runtime 29ms
# Memory 12.39MB

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        i = (len(str1) if len(str1) < len(str2) else len(str2))
        smaller = str1 if len(str1) < len(str2) else str2

        while i > 0:
            arr = str1.split(smaller[0:i])
            arr2 = str2.split(smaller[0:i])
            if len(str1)%len(smaller[:i]) == 0 and len(str2)%len(smaller[:i]) == 0:
                if not any(x != "" for x in arr) and not any(y != "" for y in arr2):
                    return smaller[:i]
            i-=1

        return ""


        