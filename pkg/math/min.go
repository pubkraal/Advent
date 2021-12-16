package math

func MinInt(iter []int) int {
	min := iter[0]
	for _, x := range iter {
		if x < min {
			min = x
		}
	}
	return min
}
