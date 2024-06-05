func containsNearbyDuplicate(nums []int, k int) bool {
	_map := make(map[int]int)
	for i, v := range nums {
		t, ok := _map[v]
		if ok && i-t <= k {
			return true
		}
		_map[v] = i
	}
	return false
}