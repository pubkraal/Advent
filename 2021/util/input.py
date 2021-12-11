def load_data(day, test=False):
    with open("./input/%02d%s.txt" % (day, "_test" if test else "")) as rd:
        return rd.readlines()


def load_ints(day, test=False):
    return list(map(int, load_data(day, test)[0].strip().split(",")))


def load_grid(day, test=False):
    return list(list(map(int, l.strip())) for l in load_data(day, test))