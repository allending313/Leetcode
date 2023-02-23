func searchInsert(nums []int, target int) int {
    head := 0
	tail := len(nums) - 1
	for head <= tail {
		mid := head + (tail-head)/2
		switch {
		case nums[mid] < target:
			head = mid + 1
		case nums[mid] > target:
			tail = mid - 1
		default:
			return mid
		}
	}
	return head
}
