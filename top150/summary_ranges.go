func summaryRanges(nums []int) []string {
	list := []string{}
	if len(nums) == 0 {
		return list
	}
	a := 0
	for i, v := range nums {
		if (i+1 >= len(nums)) || (nums[i+1] != v+1) {
			if a != i {
				list = append(list, fmt.Sprintf("%d->%d", nums[a], nums[i]))
			} else {
				list = append(list, fmt.Sprintf("%d", nums[a]))
			}
			a = i + 1
		}
	}
	return list
}