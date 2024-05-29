func canConstruct(ransomNote string, magazine string) bool {
	hashMap := make(map[string]int)
	for _, v := range magazine {
		hashMap[string(v)]++
	}

	for _, v := range ransomNote {
		if hashMap[string(v)] == 0 {
			return false
		} else {
			hashMap[string(v)]--
		}
	}
	return true
}