func minSubArrayLen(target int, nums []int) int {
    
    l, sum := 0, 0
    minLen := len(nums)+1
    
    for r := 0; r < len(nums); r++ {
        sum += nums[r]
        for sum >= target {
            if  minLen > r - l + 1 {
                minLen = r - l + 1
            }
            sum -= nums[l]
            l++
        }
    }
    
    if minLen == len(nums)+1 {
        return 0
    }
    return minLen
}