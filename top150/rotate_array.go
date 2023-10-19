func rotate(nums []int, k int) {
    n := len(nums)
    k = k % n

    // Reverse the entire slice
    reverse(nums)

    // Reverse the first k elements
    reverse(nums[:k])

    // Reverse the remaining elements
    reverse(nums[k:])
}

func reverse(nums []int) {
    for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
        nums[i], nums[j] = nums[j], nums[i]
    }
}