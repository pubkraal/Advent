package main

import (
	"fmt"
	"log"
	"math"
	"strconv"

	"github.com/pubkraal/Advent/2020/util"
)

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	nums := make([]int, len(lines))
	for idx, line := range lines {
		nums[idx], err = strconv.Atoi(line)
		if err != nil {
			log.Fatal(err)
		}
	}

	broken := 0

	for offset, num := range nums[25:] {
		combinations := util.Combinations(nums[offset:offset+25], 2)

		found := false
		for _, c := range combinations {
			if num == sum(c...) {
				found = true
				break
			}
		}

		if found {
			continue
		}

		broken = num
	}

	fmt.Println("1: ", broken)

	for _, x := range util.StartRange(2, 1000) {
		for _, y := range util.Range(len(nums) - x) {
			s := nums[x : x+y]
			t := sum(s...)
			if t == broken {
				fmt.Println("2: ", min(s...)+max(s...))
				return
			}
		}
	}
}

func sum(nums ...int) int {
	tot := 0
	for _, num := range nums {
		tot += num
	}
	return tot
}

func min(nums ...int) int {
	r := math.MaxInt32
	for _, num := range nums {
		if num < r {
			r = num
		}
	}
	return r
}

func max(nums ...int) int {
	r := math.MinInt32
	for _, num := range nums {
		if num > r {
			r = num
		}
	}
	return r
}
