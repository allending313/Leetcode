func wordPattern(pattern string, s string) bool {
	pMap := make(map[string]string)
	sMap := make(map[string]string)
	sArray := strings.Split(s, " ")

	if len(sArray) != len(pattern) {
		return false
	}
	for i, v := range pattern {
		if val, ok := pMap[string(v)]; ok {
			if val != sArray[i] {
				return false
			}
		} else {
			pMap[string(v)] = sArray[i]
		}

		if val, ok := sMap[sArray[i]]; ok {
			if val != string(pattern[i]) {
				return false
			}
		} else {
			sMap[sArray[i]] = string(pattern[i])
		}
	}
	return true
}