#!/usr/bin/env python3

def day5(filename):
    with open("input.txt", "r") as rd:
        data = rd.readlines()

    nice = [s for s in data if nice_string(s)]

    print("Step 1:", len(nice))


def nice_string(string):
    vowels = "aeiou"
    forbidden = ("ab", "cd", "pq", "xy")

    if len([l for l in string if l in vowels]) < 3:
        return False

    for x in range(len(string)-1):
        if string[x] == string[x+1]:
            break
    else:
        return False

    for x in forbidden:
        if x in string:
            return False

    return True


if __name__ == "__main__":
    assert nice_string("ugknbfddgicrmopn")
    assert nice_string("aaa")
    assert not nice_string("jchzalrnumimnmhp")
    assert not nice_string("haegwjzuvuyypxyu")
    assert not nice_string("dvszwmarrgswjxmb")
    day5("input.txt")
