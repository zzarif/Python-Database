def count_substring(string, sub_string):
    count = 0
    
    n_string = len(string)
    n_sub_string = len(sub_string)

    for i in range(n_string - n_sub_string + 1):
        for j in range(n_sub_string):
            if string[i+j] != sub_string[j]:
                break
            if j == n_sub_string - 1:
                count = count + 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))