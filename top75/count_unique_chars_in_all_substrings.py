class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        last = defaultdict(int)
        curr = defaultdict(int)

        for i, c in enumerate(s):
            curr[c] = i + 1 - last[c]
            res += sum(curr.values())

            last[c] = i + 1
        
        return res
    
    # Each character’s curr[c] tracks how many substrings ending at the current index 
    # include c as a unique character — since it last appeared. 
    # Then we sum all contributions at each step.
