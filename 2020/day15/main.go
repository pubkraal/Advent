package main

import "fmt"

func main() {
	const max = 30000000
	input := []int{9, 6, 0, 10, 18, 2, 1}
	a := make([]int, max) // all zero by default
	seen := make(map[int]int)

	for i, v := range input {
		a[i] = v
		seen[v] = i
	}

	for n := len(input); n < max-1; n++ {
		if m, ok := seen[a[n]]; ok {
			a[n+1] = n - m
		}
		seen[a[n]] = n
	}
	fmt.Println("1:", a[2019])
	fmt.Println("2:", a[29999999])
}
