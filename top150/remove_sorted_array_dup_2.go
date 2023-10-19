func removeDuplicates(nums []int) int {
    if len(nums) <= 1 {
        return len(nums)
    }
    var expected_idx = 2
    for nums_idx := 2; nums_idx < len(nums); nums_idx++ {
        if nums[nums_idx] != nums[expected_idx - 2] {
            nums[expected_idx] = nums[nums_idx]
            expected_idx += 1
        }
    }
    return expected_idx
}