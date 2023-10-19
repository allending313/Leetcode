func removeDuplicates(nums []int) int {
    var expected_idx = 0
    for _, nums_val := range(nums) {
        if nums_val > nums[expected_idx] {
            expected_idx += 1
            nums[expected_idx] = nums_val
        }
    }
    if len(nums) != 0 {
        expected_idx += 1
    }
    return expected_idx
}

