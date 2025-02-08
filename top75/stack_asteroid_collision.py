class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # i = 0
        # while i < len(asteroids) - 1:
        #     x, y = asteroids[i], asteroids[i + 1]
        #     if x > 0 and y < 0:
        #         if abs(x) > abs(y):
        #             asteroids.pop(i + 1)
        #         elif abs(x) < abs(y):
        #             asteroids.pop(i)
        #             i -= 1 if i > 0 else 0
        #         else:
        #             asteroids.pop(i)
        #             asteroids.pop(i)
        #             i -= 1 if i > 0 else 0
        #     else:
        #         i += 1
        
        # return asteroids

        s = []
        for x in asteroids:
            s.append(x)
            while len(s) > 1 and (s[-2] > 0 and s[-1] < 0):
                if abs(s[-2]) > abs(s[-1]):
                    s.pop()
                elif abs(s[-2]) < abs(s[-1]):
                    s.pop(-2)
                else:
                    s.pop()
                    s.pop()
        
        return s
