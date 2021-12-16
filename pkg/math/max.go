package math

func MaxInt(iter []int) int {
	max := iter[0]
	for _, x := range iter {
		if x > max {
			max = x
		}
	}
	return max
}
