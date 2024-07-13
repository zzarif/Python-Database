if __name__ == "__main__":
    setA = set(input().split())
    n = int(input())
    is_a_strict_superset = True
    for _ in range(n):
        setB = set(input().split())
        if is_a_strict_superset:
            if len(setB) < len(setA):
                setB.difference_update(setA)
                is_a_strict_superset = len(setB) == 0
            else:
                is_a_strict_superset = False
    print(is_a_strict_superset)