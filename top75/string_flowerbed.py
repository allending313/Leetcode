class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # zeros = ''.join(map(str, flowerbed))
        # zeros = '0' + zeros + '0'

        # for x in zeros.split('1'):
        #     if (z := len(x)) >= 3:
        #         n -= (z - 1) // 2
        
        # return n <= 0
        
        flowerbed = [0] + flowerbed + [0]
        i = 1
        while i < len(flowerbed) - 1:
            # if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
            #     n -= 1
            #     i += 1
            # i += 1

            if flowerbed[i] == 1:
                i += 1
            elif flowerbed[i + 1] == 1:
                i += 2
            elif flowerbed[i - 1] != 1:
                n -= 1
                i += 1
            i += 1
            
        return n <= 0            
            
