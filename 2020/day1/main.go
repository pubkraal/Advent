package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/pubkraal/Advent/2020/util"
)

func getNumbers(filename string) ([]int, error) {
	numbers := make([]int, 0)
	file, err := os.Open(filename)
	if err != nil {
		return []int{}, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		num, err := strconv.Atoi(line)
		if err != nil {
			return []int{}, err
		}
		numbers = append(numbers, num)
	}
	return numbers, nil
}

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
	numbers, err := getNumbers("input.txt")
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
