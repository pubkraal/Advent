package main

import (
	"fmt"
	"log"

	"github.com/pubkraal/Advent/2020/util"
)

type record struct {
	min      int
	max      int
	letter   rune
	password string
}

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	validPasswords := make([]*record, 0)
	validNewPasswords := make([]*record, 0)

	for _, line := range lines {
		rec := &record{}
		_, err := fmt.Sscanf(line, "%d-%d %c: %s",
			&rec.min, &rec.max, &rec.letter, &rec.password)
		if err != nil {
			log.Fatal(err)
		}

		if rec.ValidStepOne() {
			validPasswords = append(validPasswords, rec)
		}
		if rec.ValidStepTwo() {
			validNewPasswords = append(validNewPasswords, rec)
		}
	}
	fmt.Println("Valid 1", len(validPasswords))
	fmt.Println("Valid 2", len(validNewPasswords))
	fmt.Println("Total  ", len(lines))
}

func (r *record) ValidStepOne() bool {
	count := 0
	for _, letter := range r.password {
		if letter == r.letter {
			count++
		}
	}

	return count >= r.min && count <= r.max
}

func (r *record) ValidStepTwo() bool {
	count := 0
	runes := []rune(r.password)
	for _, x := range []int{r.min, r.max} {
		if runes[x-1] == r.letter {
			count++
		}
	}
	return count == 1
}
