package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
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

func main() {
	numbers, err := getNumbers("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	for _, num1 := range numbers {
		for _, num2 := range numbers {
			if num1+num2 == 2020 {
				fmt.Println("Result 1:", num1*num2, num1, num2)
			}
			for _, num3 := range numbers {
				if num1+num2+num3 == 2020 {
					fmt.Println("Result 2:", num1*num2*num3, num1, num2, num3)
				}
			}

		}
	}
}
