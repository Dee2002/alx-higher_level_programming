#!/usr/bin/python3
import sys

def print_alphabet(start):
    if start <= ord('Z'):
        sys.stdout.write(chr(start))
        print_alphabet(start + 1)

print_alphabet(ord('A'))
