import numpy as np


if __name__ == "__main__":
    a = np.array([2,3,4,5])
    b = a.copy()
    print(a)
    print(b)
    a[0] = -5
    print()
    print(a)
    print(b)