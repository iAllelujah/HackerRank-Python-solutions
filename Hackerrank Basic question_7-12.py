#Q1.
"""Given the participants score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
INPUT FORMAT:
The first line contains n. The second line contains an array A[] of n integers each separated by a space."""
#SOLUTION
"""n = int(input())
arr = map(int, input().split())
scores = list(arr)
score1 = max(scores)

while score1 in scores:
    scores.remove(score1)
score2 = max(scores)
print(score2)"""

#Q2
"""In a 20 over cricket match, the batting team is scroing runs at sum run rate. 
WAP to predict total runs scored by the team at the end if run rate dosent change between overs. """
"""def match(RR):
    Score=RR*20
    print(Score)
match(float(input("Enter the run rate")))"""

#Q3
"""Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line."""
#SOLUTION
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

grades = sorted(set(student[1] for student in students))
second_lowest_grade = grades[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
second_lowest_students.sort()
for student in second_lowest_students:
    print(student)