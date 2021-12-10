package functional

func ZipInt(inputs ...[]int) [][]int {
	uselen := 2147483647
	for _, inp := range inputs {
		if len(inp) < uselen {
			uselen = len(inp)
		}
	}

	ret := make([][]int, uselen)

	for i := 0; i < uselen; i++ {
		tmp := make([]int, len(inputs))
		for j := 0; j < len(inputs); j++ {
			tmp[j] = inputs[j][i]
		}
		ret[i] = tmp
	}
	return ret
}
