if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    output_scores = student_marks[query_name]
    avg_score = sum(output_scores)/len(output_scores)

    print("%.2f" % avg_score)