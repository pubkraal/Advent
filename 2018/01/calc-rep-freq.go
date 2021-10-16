package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func find_rep_freq(start int, filename string) {
	changes := build_freq_adjustments(filename)
	len_ch := len(changes)

	current := start
	counter := 0
	found := make(map[int]bool)
	for {
		mut := changes[counter%len_ch]
		counter = counter + 1
		current = current + mut
		_, ok := found[current]
		if ok {
			break
		}
		found[current] = true
	}

	fmt.Println("01:2 = ", current)
}

func build_freq_adjustments(filename string) []int {
	reslist := make([]int, 0)

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		reslist = append(reslist, i)
	}

	return reslist
}
