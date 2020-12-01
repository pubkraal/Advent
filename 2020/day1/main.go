package main

import (
	"fmt"
	"log"

	"github.com/pubkraal/Advent/2020/util"
)

func sum(nums ...int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

func prod(nums ...int) int {
	total := 1
	for _, num := range nums {
		total *= num
	}
	return total
}

func main() {
	numbers, err := util.GetNumbers("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	for _, size := range []int{2, 3} {
		combis := util.ChannelCombinations(numbers, size)
		for combi := range combis {
			if sum(combi...) == 2020 {
				fmt.Println("For size", size, "product is", prod(combi...))
				break
			}
		}
	}
}
