import os


def file_to_day(filepath):
    head, tail = os.path.split(filepath)
    day = tail.split(".")[0]
    return int(day)