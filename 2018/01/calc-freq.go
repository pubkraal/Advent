package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) >= 2 {
		calculate_freq(0, os.Args[1])
	} else {
		fmt.Println("Please also give us a file to understand....")
	}
}

func calculate_freq(start int, inputfile string) {
	current := start

	file, err := os.Open(inputfile)
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
		current = current + i
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Resulting frequency:", current)
}
