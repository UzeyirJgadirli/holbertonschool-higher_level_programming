#!/usr/bin/python3
"""Print all names defined by hidden_4.pyc"""

import hidden_4
import inspect

if __name__ == "__main__":
    names = [name for name, obj in inspect.getmembers(hidden_4)]
    names = [name for name in names if not name.startswith("__")]
    for name in sorted(names):
        print(name)
