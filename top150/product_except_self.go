func productExceptSelf(nums []int) []int {
    len := len(nums)
    res := make([]int, len)
    res[0] = 1
    rightProduct := 1

    // left product accumulation
    for i := 1; i < len; i++ {
        res[i] = res[i-1] * nums[i-1]
    }

    // right product accumulation
    for i := len - 2; i >= 0; i-- {
        rightProduct *= nums[i+1]
        res[i] *= rightProduct
    }

    return res
}