#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    module_attrs = dir(hidden_4)
    for attr in sorted(module_attrs):
        if not attr.startswith("__"):
            print(attr)
