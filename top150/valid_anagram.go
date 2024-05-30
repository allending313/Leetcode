func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sMap := make(map[byte]int)
	for i := range s {
		if s[i] != t[i] {
			sMap[s[i]]++
			sMap[t[i]]--
		}
	}
	for _, v := range sMap {
		if v != 0 {
			return false
		}
	}
	return true
}