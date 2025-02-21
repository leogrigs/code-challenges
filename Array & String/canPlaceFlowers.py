# Runtime 51ms
# Memory 12.62MB

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        counter, i = 0, 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # left
                left = False
                if i > 0:
                    if flowerbed[i-1] == 0:
                        left = True
                else:
                    left = True
                
                #right
                right = False
                if i != len(flowerbed) - 1:
                    if flowerbed[i+1] == 0:
                        right = True
                else:
                    right = True

                if right and left:
                    print(i)
                    counter += 1
                    i += 1
                
            i += 1

        return counter >= n

        