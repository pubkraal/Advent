package util

import "sort"

// Combinations returns all combinations of a given slice of ints.
// Dutifully stolen from python: https://docs.python.org/3/library/itertools.html#itertools.combinations
func Combinations(numbers []int, r int) [][]int {
	n := len(numbers)
	if r > n {
		return [][]int{}
	}

	indices := Range(r)
	reversed := Range(r)
	sort.Sort(sort.Reverse(sort.IntSlice(reversed)))
	sets := make([][]int, 0)
	sets = append(sets, combination(numbers, indices))

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
			return sets
		}

		indices[lastnum] += 1
		for _, j := range StartRange(lastnum+1, r) {
			indices[j] = indices[j-1] + 1
		}
		sets = append(sets, combination(numbers, indices))
	}
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
