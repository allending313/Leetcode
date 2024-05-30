// save some memory by using one hashmap and running isIsomorphic on both strings
func isIsomorphic(s string, t string) bool {
	_map := make(map[string]string)

	for i, v := range s {
		if _map[string(v)] == "" {
			_map[string(v)] = string(t[i])
		}
		if _map[string(v)] != string(t[i]) {
			return false
		}
	}

	clear(_map)
	for i, v := range t {
		if _map[string(v)] == "" {
			_map[string(v)] = string(s[i])
		}
		if _map[string(v)] != string(s[i]) {
			return false
		}
	}
	return true
}

// faster run via one pass leveraging two hashmaps for the two strings
func isIsomorphic(s string, t string) bool {
	sMap := make(map[byte]byte, len(s))
	tMap := make(map[byte]byte, len(s))

	for i, _ := range s {
		_, sOK := sMap[s[i]]
		_, tOK := tMap[t[i]]

		if !sOK && !tOK {
			// if char isn't found in both maps
			sMap[s[i]] = t[i]
			tMap[t[i]] = s[i]

		} else if sOK {
			//if found in sMap but the char isn't same as existing
			if sMap[s[i]] != t[i] {
				return false
			}

		} else if tOK {
			//if found in tMap but the char isn't same as existing
			if tMap[t[i]] != s[i] {
				return false
			}
		}
	}

	return true
}