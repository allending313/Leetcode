func titleToNumber(s string) int {
    res := 0
    for _, c := range s {
        res *= 26
        res += int(c - 'A') + 1
    }
    return res
}