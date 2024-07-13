if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    
    my_list = list(arr)
    my_list.sort(reverse=True)

    for item in my_list:
        if item < my_list[0]:
            print(item)
            break
