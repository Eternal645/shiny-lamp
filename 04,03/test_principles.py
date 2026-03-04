import sys
sys.path.append("../../src")

from math_add import (add, add_with_bug)

def test_add():
    assert add(2, 2) == 4

if __name__ == "__main__":
    test_add()