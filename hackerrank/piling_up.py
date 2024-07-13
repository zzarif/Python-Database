import sys


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        my_list = list(map(int, input().split()))
        possible = "Yes"
        i = 0
        j = len(my_list) - 1
        current_top = sys.maxsize
        while i <= j:
            if my_list[i] > my_list[j] and my_list[i] <= current_top:
                current_top = my_list[i]
                i = i + 1
            elif my_list[j] <= current_top:
                current_top = my_list[j]
                j = j - 1
            else:
                possible = "No"
                break
        print(possible)
