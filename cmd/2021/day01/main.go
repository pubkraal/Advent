package main

import (
	"flag"
	"log"

	"github.com/pubkraal/Advent/pkg/functional"
	"github.com/pubkraal/Advent/pkg/input"
	"github.com/pubkraal/Advent/pkg/math"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}
	nums := input.GetIntLines(args[0])
	sumint := make([]int, len(nums)-2)
	for idx, val := range functional.ZipInt(nums, nums[1:], nums[2:]) {
		sumint[idx] = math.SumInt(val)
	}
	log.Printf("2021:01:1 = %d", getIncs(nums))
	log.Printf("2021:01:2 = %d", getIncs(sumint))
}

func getIncs(nums []int) int {
	numinc := 0
	prev := 2147483647
	for _, num := range nums {
		if num > prev {
			numinc += 1
		}
		prev = num
	}
	return numinc
}
