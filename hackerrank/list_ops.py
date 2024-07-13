if __name__ == "__main__":
    n = int(input())
    my_list = []
    for _ in range(n):
        command, *line = input().split()
        match command:
            case "insert":
                operands = list(map(int,line))
                my_list.insert(operands[0], operands[1])
            case "print":
                print(my_list)
            case "remove":
                my_list.remove(int(line[0]))
            case "append":
                my_list.append(int(line[0]))
            case "sort":
                my_list.sort()
            case "pop":
                my_list.pop()
            case "reverse":
                my_list.reverse()