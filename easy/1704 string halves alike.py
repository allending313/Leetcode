class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        """ trash
        half = len(s)//2
        counter = 0
        for i in range(half):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                counter += 1
        for i in range(half, len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                counter -= 1
                
        return True if counter == 0 else False
        """
        
        # slightly cleaner version of the above albeit slightly slower
        vowels = "aeiouAEIOU"
        mid, ans = len(s) // 2, 0
        for i in range(mid):
            if s[i] in vowels: ans += 1
            if s[mid+i] in vowels: ans -=1
        return ans == 0