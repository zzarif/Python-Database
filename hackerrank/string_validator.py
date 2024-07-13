if __name__ == "__main__":
    s = input().strip()
    validation = [False, False, False, False, False]

    for i in range(len(s)):
        if s[i].isalnum():
            validation[0] = True
        if s[i].isalpha():
            validation[1] = True
        if s[i].isdigit():
            validation[2] = True
        if s[i].islower():
            validation[3] = True
        if s[i].isupper():
            validation[4] = True
    for val in validation:
        print(val)