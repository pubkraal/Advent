package main

import (
	"flag"
	"fmt"
	"log"
	"strconv"

	"github.com/pubkraal/Advent/pkg/input"
	"github.com/pubkraal/Advent/pkg/math"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}
	instructions := []string{toBinRepr(input.GetLines(args[0])[0])}
	sum, output := parse(&instructions)
	fmt.Println("2021:16:1 =", sum)
	fmt.Println("2021:16:2 =", output)
}

func peek(data *[]string, n int) string {
	pk := (*data)[0][:n]
	(*data)[0] = (*data)[0][n:]
	return pk
}

func mustPeekInt(data *[]string, n int) int {
	pk := peek(data, n)
	num, err := strconv.ParseInt(pk, 2, 64)
	if err != nil {
		panic(err)
	}

	return int(num)
}

func parse(instructions *[]string) (sumversions, result int64) {
	ver := peek(instructions, 3)
	version, _ := strconv.ParseInt(ver, 2, 16)
	sumversions += version

	typeID := mustPeekInt(instructions, 3)
	if typeID == 4 {
		num := ""
		for {
			p := peek(instructions, 5)
			n := p[1:]
			num = fmt.Sprintf("%s%s", num, n)
			if p[0] == '0' {
				break
			}
		}
		return sumversions, int64(mustParseBin(num))
	}

	lengthTypeID := peek(instructions, 1)
	spv := make([]int, 0)
	if lengthTypeID == "0" {
		lenSubpackets := mustPeekInt(instructions, 15)
		subpackets := []string{peek(instructions, lenSubpackets)}
		for len(subpackets[0]) > 0 {
			sv, r := parse(&subpackets)
			spv = append(spv, int(r))
			sumversions += sv
		}
	} else {
		numPackets := mustPeekInt(instructions, 11)
		for i := 0; i < numPackets; i++ {
			sv, r := parse(instructions)
			spv = append(spv, int(r))
			sumversions += sv
		}
	}

	switch typeID {
	case 0:
		return sumversions, int64(math.SumInt(spv))
	case 1:
		var p int64 = 1
		for _, x := range spv {
			p *= int64(x)
		}
		return sumversions, p
	case 2:
		return sumversions, int64(math.MinInt(spv))
	case 3:
		return sumversions, int64(math.MaxInt(spv))
	case 5:
		if spv[0] > spv[1] {
			return sumversions, 1
		}
		return sumversions, 0
	case 6:
		if spv[0] < spv[1] {
			return sumversions, 1
		}
		return sumversions, 0
	case 7:
		if spv[0] == spv[1] {
			return sumversions, 1
		}
		return sumversions, 0
	}

	return sumversions, result
}

func mustParseBin(in string) int {
	r, err := strconv.ParseInt(in, 2, 64)
	if err != nil {
		panic(err)
	}
	return int(r)
}

func toBinRepr(input string) string {
	output := ""
	for _, c := range input {
		n, _ := strconv.ParseInt(string(c), 16, 64)
		output = fmt.Sprintf("%s%s", output, binaryZeroPrefix(n, 4))
	}
	return output
}

func binaryZeroPrefix(in int64, size int) string {
	output := strconv.FormatInt(in, 2)
	if len(output) < size {
		need := size - len(output)
		for i := 0; i < need; i++ {
			output = fmt.Sprintf("%d%s", 0, output)
		}
	}
	return output
}
