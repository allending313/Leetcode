func canJump(nums []int) bool {
    end := len(nums) - 1
    for i := end - 1; i >= 0; i-- {
        if nums[i] >= end - i {
            end = i
        }
    }
    return end == 0
}
