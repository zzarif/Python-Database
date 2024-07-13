if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    my_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

    ## equivalent nested for loops
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i + j + k != n:
    #                 my_list.append([i, j, k])

                
    print(my_list)