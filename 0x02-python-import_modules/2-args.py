#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{} argument{}".format(argc, "s" if argc != 1 else ""), end="")
    print("." if argc == 0 else ":")
    
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
