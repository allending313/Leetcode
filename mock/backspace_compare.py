class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # iterate backwards through both strings with pointers
        # if we encounter a # then move the pointer one more to the left
        # match each char

        x = len(s) - 1
        y = len(t) - 1
        skip_x = 0
        skip_y = 0

        while x >= 0 or y >= 0:
            if x >= 0:
                if s[x] == '#':
                    skip_x += 1
                    x -= 1
                    continue
                if skip_x > 0:
                    x -= 1
                    skip_x -= 1
                    continue
            
            if y >= 0:
                if t[y] == '#':
                    skip_y += 1
                    y -= 1
                    continue
                if skip_y > 0:
                    y -= 1
                    skip_y -= 1
                    continue
                
            if x >= 0 and y >= 0 and s[x] != t[y]:
                return False
            
            x -= 1
            y -= 1
        
        if x < 0 and x == y:
            return True
        return False
        
