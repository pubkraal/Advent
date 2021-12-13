.PHONY: all test 2021

2021=$(shell find 2021/input -name *.txt -exec basename {} + | egrep -o '[0-9]+' | sort -n | uniq)
PKG=$(shell find pkg -name *.go)

all: target/2021/day01 target/2021/day02 target/2021/day03 target/2021/day10 target/2021/day12 target/2021/day13

test:
	go test -v ./...

target/2021/day01: ${PKG} cmd/2021/day01/*.go
	go build -o target/2021/day01 ./cmd/2021/day01

target/2021/day02: ${PKG} cmd/2021/day02/*.go
	go build -o target/2021/day02 ./cmd/2021/day02

target/2021/day03: ${PKG} cmd/2021/day03/*.go
	go build -o target/2021/day03 ./cmd/2021/day03

target/2021/day12: ${PKG} cmd/2021/day12/*.go
	go build -o target/2021/day12 ./cmd/2021/day12

target/2021/day13: ${PKG} cmd/2021/day13/*.go
	go build -o target/2021/day13 ./cmd/2021/day13