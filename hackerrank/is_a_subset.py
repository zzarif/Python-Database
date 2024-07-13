if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n_a = int(input())
        setA = set(input().split())
        n_b = int(input())
        setB = set(input().split())
        setA.difference_update(setB)
        print(len(setA) == 0)

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2