def longest_valid_string(s: str) -> str:
    n = len(s)
    if n < 3:
        return s
    
    res = s[:2]
    
    prev1 = s[1]
    prev2 = s[0]

    for i in range(2, n):
        if s[i] == prev1 and s[i] == prev2:
            continue
        res += s[i]
        prev2 = prev1
        prev1 = s[i]
    
    return res
