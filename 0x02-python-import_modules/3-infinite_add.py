#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("0")
    else:
        result = sum(map(int, args))
        print(result)
