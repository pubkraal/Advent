package main

import (
	"flag"
	"fmt"
	"log"
	"strings"

	"github.com/pubkraal/Advent/pkg/data"
	"github.com/pubkraal/Advent/pkg/input"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	nodes := make(map[string][]string)

	for _, line := range input.GetLines(args[0]) {
		parts := strings.Split(line, "-")
		parent := parts[0]
		child := parts[1]

		if _, ok := nodes[parent]; !ok {
			nodes[parent] = []string{child}
		} else {
			nodes[parent] = append(nodes[parent], child)
		}
		if _, ok := nodes[child]; !ok {
			nodes[child] = []string{parent}
		} else {
			nodes[child] = append(nodes[child], parent)
		}
	}

	visited := make(map[string]bool)
	p1 := search(nodes, "start", visited, false, "")
	p2 := search(nodes, "start", visited, true, "")

	fmt.Println("2021:12:1 =", len(p1))
	fmt.Println("2021:12:2 =", len(p2))
}

func search(nodes map[string][]string, root string, visited map[string]bool, part2 bool, little string) [][]string {
	paths := make([][]string, 0)
	visited[root] = true

	for _, node := range nodes[root] {
		if node == "end" {
			paths = append(paths, []string{root})
		} else if node == "start" {
			continue
		} else if node != strings.ToLower(node) {
			visitCopy := data.CopyCheapSet(visited)
			paths = append(paths, search(nodes, node, visitCopy, part2, little)...)
		} else {
			if _, ok := visited[node]; ok {
				if part2 && little == "" {
					visitCopy := data.CopyCheapSet(visited)
					paths = append(paths, search(nodes, node, visitCopy, part2, node)...)
				}
			} else {
				visitCopy := data.CopyCheapSet(visited)
				paths = append(paths, search(nodes, node, visitCopy, part2, little)...)
			}
		}
	}

	return paths
}
