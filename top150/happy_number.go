func isHappy(n int) bool {
	visited := map[int]bool{}
	for {
		nextValue := 0
		for ; n > 0; n = n / 10 {
			nextValue += (n % 10) * (n % 10)
		}

		if _, ok := visited[nextValue]; ok {
			return nextValue == 1
		} else {
			visited[nextValue] = true
		}

		n = nextValue
	}

	return false
}