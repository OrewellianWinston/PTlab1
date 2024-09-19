# -*- coding: utf-8 -*-
import argparse
import sys

# from TextDataReader import TextDataReader
from .JSONDataReader import JSONReader
from .QuartilleCalc import QuartilleCalc


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = JSONReader()
    students = reader.read(path)
    print("Students: ", students)
    quartille_calc = QuartilleCalc(students)
    last_quartile_students = quartille_calc.compare()

    print("Rating: ", last_quartile_students)


if __name__ == "__main__":
    main()
