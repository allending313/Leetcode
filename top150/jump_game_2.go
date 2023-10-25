/* brute force

func jump(nums []int) int {
    res := 0
    end := len(nums) - 1
    for end > 0 {
        for i := 0; i < end; i++ {
            if nums[i] + i >= end {
                end = i
                res++
            }
        }
    }
    return res
}

*/

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func jump(nums []int) int {
    far, res, end := 0, 0, 0
    for i := 0; i < len(nums)-1; i++ {
        far = Max(far, i + nums[i])
        if i == end {
            res++
            end = far
        }
    }
    return res
}