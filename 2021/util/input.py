def load_data(day, test=False):
    with open("./input/%02d%s.txt" % (day, "_test" if test else "")) as rd:
        return rd.readlines()
