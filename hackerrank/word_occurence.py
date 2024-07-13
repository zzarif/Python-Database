if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(n)]
    word_occurence = {}
    for word in words:
        if word in word_occurence:
            word_occurence[word] += 1
        else:
            word_occurence[word] = 1
    
    print(len(word_occurence))
    for key, value in word_occurence.items():
        print(value, end=' ')
    print()