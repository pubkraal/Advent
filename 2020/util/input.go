package util

import (
	"bufio"
	"os"
	"strconv"
)

func GetNumbers(filename string) ([]int, error) {
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

func GetLines(filename string) ([]string, error) {
	lines := make([]string, 0)
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	return lines, nil
}
