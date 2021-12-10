package math

func SumInt(nums []int) int {
	tot := 0
	for _, x := range nums {
		tot += x
	}
	return tot
}
