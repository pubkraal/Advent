package main

import (
	"crypto/md5"
	"fmt"
)

func main() {
	secret := "iwrupvqb"

	index := 0
	found5 := false

	for {
		h := md5.Sum([]byte(fmt.Sprintf("%s%d", secret, index)))
		d := fmt.Sprintf("%x", h)

		if d[:6] == "000000" {
			fmt.Println("Step 2:", index)
			break
		}
		if !found5 && d[:5] == "00000" {
			fmt.Println("Step 1:", index)
			found5 = true
		}
		index++
	}
}
