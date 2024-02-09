func maxArea(height []int) int {
    l, r := 0, len(height)-1 
    m := 0

    for l < r {
        if s := min(height[l], height[r]) * (r-l); s > m {
            m = s
        }
        if height[l] > height[r] {
            r--
        } else {
            l++
        }
    }
    return m
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}