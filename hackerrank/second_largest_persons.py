# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == "__main__":
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]
    rev_students = [[score, name] for name, score in students]
    rev_students.sort()

    lowest_score = rev_students[0][0]

    for score, name in rev_students:
        if score > lowest_score:
            second_lowest_score = score
            break
    
    wanted_students = [name for score, name in rev_students if score == second_lowest_score]

    wanted_students.sort()

    for student in wanted_students:
        print(student)