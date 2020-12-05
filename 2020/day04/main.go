package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/2020/util"
)

func ValidPassportStepOne(passport map[string]string) bool {
	requiredFields := []string{
		"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, field := range requiredFields {
		_, ok := passport[field]
		if !ok {
			return false
		}
	}
	return true
}

func ValidPassportStepTwo(passport map[string]string) bool {
	requiredFields := []string{
		"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, field := range requiredFields {
		val, ok := passport[field]
		if !ok {
			return false
		}
		if !ValidateValue(field, val) {
			return false
		}
	}
	return true
}

func ValidateValue(name, value string) bool {
	switch name {
	case "byr":
		rval, _ := strconv.Atoi(value)
		if rval >= 1920 && rval <= 2002 {
			return true
		}
	case "iyr":
		rval, _ := strconv.Atoi(value)
		if rval >= 2010 && rval <= 2020 {
			return true
		}
	case "eyr":
		rval, _ := strconv.Atoi(value)
		if rval >= 2020 && rval <= 2030 {
			return true
		}
	case "hgt":
		lower, upper := 100, 150
		var ival string
		switch {
		case strings.HasSuffix(value, "in"):
			lower, upper = 59, 76
			ival = strings.TrimSuffix(value, "in")
		case strings.HasSuffix(value, "cm"):
			lower, upper = 150, 193
			ival = strings.TrimSuffix(value, "cm")
		default:
			log.Println("hgt invalid: " + value)
		}
		rval, _ := strconv.Atoi(ival)
		if rval >= lower && rval <= upper {
			return true
		}
	case "hcl":
		matched, _ := regexp.Match(`#([0-9a-f]{6})`, []byte(value))
		return matched
	case "ecl":
		allowed := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
		for _, val := range allowed {
			if value == val {
				return true
			}
		}
		return false
	case "pid":
		matched, _ := regexp.Match(`^[0-9]{9}$`, []byte(value))
		return matched
	}
	return false
}

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	passports := parsePassports(lines)

	validOne := 0
	validTwo := 0
	for _, pass := range passports {
		if ValidPassportStepOne(pass) {
			validOne++
			if ValidPassportStepTwo(pass) {
				validTwo++
			}
		}
	}
	fmt.Println("Total :", len(passports))
	fmt.Println("Step 1:", validOne)
	fmt.Println("Step 1:", validTwo)
}

func parsePassports(lines []string) []map[string]string {
	ps := make([]map[string]string, 0)

	pass := make(map[string]string)

	for _, line := range lines {
		if line == "" {
			ps = append(ps, pass)
			pass = make(map[string]string)
			continue
		}

		kvs := strings.Split(line, " ")
		for _, kv := range kvs {
			set := strings.Split(kv, ":")
			pass[set[0]] = set[1]
		}
	}

	return ps
}
