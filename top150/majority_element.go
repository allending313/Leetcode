func majorityElement(nums []int) int {
    // Boyer-Moore Majority Vote algorithm
    candidate := nums[0]
	count := 1
	for _, num := range nums[1:] {
		if num == candidate {
			count++
		} else {
			count--
		}
		if count == 0 {
			candidate = num
			count = 1
		}
	}
	return candidate
}