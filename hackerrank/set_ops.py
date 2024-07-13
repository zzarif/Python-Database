if __name__ == "__main__":
    n_a = int(input())
    a = set(map(int, input().split()))
    n_o = int(input())
    for _ in range(n_o):
        operation, n_b = input().split()
        b = set(map(int, input().split()))
        match operation:
            case "intersection_update":
                a.intersection_update(b)
                # a &= b
            case "update":
                a.update(b)
                # a |= b
            case "symmetric_difference_update":
                a.symmetric_difference_update(b)
                # a ^= b
            case "difference_update":
                a.difference_update(b)
                # a -= b
    print(sum(a))