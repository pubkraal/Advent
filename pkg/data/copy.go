package data

func CopyCheapSet(in map[string]bool) map[string]bool {
	ret := make(map[string]bool)
	for key, value := range in {
		ret[key] = value
	}
	return ret
}
