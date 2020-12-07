package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"

	"github.com/pubkraal/Advent/2020/util"
)

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	data, err := compileData(lines)
	if err != nil {
		log.Fatal(err)
	}

	s1 := unique(contains(data, "shiny gold"))
	s2 := number(data, "shiny gold")
	fmt.Println("Step 1:", len(s1)-1)
	fmt.Println("Step 2:", s2)
}

func number(data map[string]map[string]int, search string) int {
	tots := 0

	for key, value := range data[search] {
		tots += value * (1 + number(data, key))
	}
	return tots
}

func unique(in []string) []string {
	tmp := make(map[string]bool)
	for _, v := range in {
		tmp[v] = true
	}

	out := make([]string, 0)
	for k := range tmp {
		out = append(out, k)
	}
	return out
}

func contains(data map[string]map[string]int, search string) []string {
	traits := make([]string, 0)

	for key, sub := range data {
		if _, ok := sub[search]; ok {
			traits = append(traits, key)
		}

	}

	for _, tr := range traits {
		sub := contains(data, tr)
		traits = append(traits, sub...)
	}

	retval := make([]string, 0)
	retval = append(retval, search)
	retval = append(retval, traits...)

	return retval
}

func compileData(lines []string) (map[string]map[string]int, error) {
	tre, err := regexp.Compile(`(\w+ \w+)`)
	if err != nil {
		return nil, err
	}
	subs, err := regexp.Compile(`(\d+) (\w+ \w+)`)
	if err != nil {
		return nil, err
	}

	data := make(map[string]map[string]int)

	for _, line := range lines {
		ident := tre.FindString(line)
		inside := subs.FindAllStringSubmatch(line, -1)

		x := make(map[string]int)
		for _, i := range inside {
			num, err := strconv.Atoi(i[1])
			if err != nil {
				return nil, err
			}
			x[i[2]] = num
		}

		data[ident] = x
	}
	return data, nil
}
