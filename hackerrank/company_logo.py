from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    char_counts = Counter(s).most_common() # tuple: [('k', 9), ('j', 5)]

    sorted_char_counts = sorted(char_counts, key=lambda x: (x[1] * -1, x[0]))

    for char in sorted_char_counts[:3]:
        print(char[0], char[1])
