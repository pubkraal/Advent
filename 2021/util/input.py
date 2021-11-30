def load_data(day):
    with open("./input/%02d.txt" % (day,)) as rd:
        return rd.readlines()
