func threeSum(nums []int) [][]int {
	l := [][]int{}
	n := len(nums)
	sort.Ints(nums)

	for i := range nums {
        // skip duplicates
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}

		j, k := i+1, n-1
		for j < k {
			if sum := nums[i] + nums[j] + nums[k]; sum > 0 {
				k--
			} else if sum < 0 {
				j++
			} else {
				l = append(l, []int{nums[i], nums[j], nums[k]})
				j++
				for nums[j-1] == nums[j] && j < k {
					j++
				}
			}

		}
	}

	return l
}