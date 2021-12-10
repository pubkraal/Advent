package input

import (
	"bufio"
	"os"
	"strconv"
)

func GetIntLines(filename string) []int {
	lines := make([]int, 0)
	file := mustOpen(filename)
	defer func() {
		_ = file.Close()
	}()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			panic(err)
		}
		lines = append(lines, int(line))
	}
	return lines
}

func GetLines(filename string) []string {
	lines := make([]string, 0)
	file := mustOpen(filename)
	defer func() {
		_ = file.Close()
	}()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func mustOpen(filename string) *os.File {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	return file
}
