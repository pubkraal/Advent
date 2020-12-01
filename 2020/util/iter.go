package util

import "sort"

// Combinations returns all combinations of a given slice of ints.
// Dutifully stolen from python: https://docs.python.org/3/library/itertools.html#itertools.combinations
func Combinations(numbers []int, r int) [][]int {
	sets := make([][]int, 0)
	for set := range ChannelCombinations(numbers, r) {
		sets = append(sets, set)
	}

	return sets
}

func ChannelCombinations(numbers []int, r int) <-chan []int {
	out := make(chan []int)
	go func() {
		n := len(numbers)
		if r > n {
			close(out)
			return
		}

		indices := Range(r)
		reversed := Range(r)
		sort.Sort(sort.Reverse(sort.IntSlice(reversed)))
		out <- combination(numbers, indices)

		for {
			found := false
			lastnum := 0
			for _, i := range reversed {
				if indices[i] != i+n-r {
					found = true
					lastnum = i
					break
				}
			}
			if !found {
				close(out)
				return
			}

			indices[lastnum] += 1
			for _, j := range StartRange(lastnum+1, r) {
				indices[j] = indices[j-1] + 1
			}
			out <- combination(numbers, indices)
		}
	}()
	return out
}

func combination(pool, indices []int) []int {
	nums := make([]int, len(indices))
	for idx, val := range indices {
		nums[idx] = pool[val]
	}
	return nums
}

func Range(max int) []int {
	num := make([]int, max)
	for cur := 0; cur < max; cur++ {
		num[cur] = cur
	}
	return num
}

func StartRange(min, max int) []int {
	if max <= min {
		return []int{}
	}
	size := max - min
	num := make([]int, size)
	for cur := 0; cur < size; cur++ {
		num[cur] = cur + min
	}
	return num
}
