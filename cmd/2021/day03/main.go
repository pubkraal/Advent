package main

import (
	"flag"
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/pkg/input"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	lines := input.GetLines(args[0])
	numLines := len(lines)
	sums := sumBits(lines)
	compute := make([]string, 12)
	for idx, sum := range sums {
		if float64(sum)/float64(numLines) > 0.5 {
			compute[idx] = "1"
		} else {
			compute[idx] = "0"
		}
	}
	gamma, err := strconv.ParseInt(strings.Join(compute, ""), 2, 64)
	if err != nil {
		panic(err)
	}
	p1 := gamma * (gamma ^ 0b111111111111)

	o2res := make([]int, 12)
	co2res := make([]int, 12)
	o2bits := make([]string, len(lines))
	co2bits := make([]string, len(lines))
	copy(o2bits, lines)
	copy(co2bits, lines)

	for i := 0; i < 12; i++ {
		o2sums := sumBits(o2bits)
		cur := 0
		if float64(o2sums[i])/float64(len(o2bits)) >= 0.5 {
			cur = 1
		}
		o2res[i] = cur
		o2bits = filterBits(o2bits, buildPrefix(o2res, i))
	}

	for i := 0; i < 12; i++ {
		co2sums := sumBits(co2bits)
		cur := 0
		if float64(co2sums[i])/float64(len(co2bits)) < 0.5 {
			cur = 1
		}

		co2res[i] = cur
		co2bits = filterBits(co2bits, buildPrefix(co2res, i))
		if len(co2bits) == 1 {
			for idx, r := range co2bits[0] {
				co2res[idx] = 0
				if r == '1' {
					co2res[idx] = 1
				}
			}
			break
		}
	}

	o2p, _ := strconv.ParseInt(buildPrefix(o2res, 11), 2, 64)
	co2p, _ := strconv.ParseInt(buildPrefix(co2res, 11), 2, 64)
	p2 := o2p * co2p
	fmt.Println("2021:03:1 =", p1)
	fmt.Println("2021:03:2 =", p2)
}

func buildPrefix(nums []int, stop int) string {
	tmp := ""
	for i := 0; i <= stop; i++ {
		tmp = fmt.Sprintf("%s%d", tmp, nums[i])
	}
	return tmp
}

func filterBits(lines []string, prefix string) []string {
	ret := make([]string, 0)
	for _, line := range lines {
		if strings.HasPrefix(line, prefix) {
			ret = append(ret, line)
		}
	}
	return ret
}

func sumBits(lines []string) []int {
	out := make([]int, 12)
	for _, line := range lines {
		for idx, r := range line {
			val := 0
			if r == '1' {
				val = 1
			}
			out[idx] += val
		}
	}
	return out
}
