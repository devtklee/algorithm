'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1088 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1088

Date : 2021-02-15
Solved BY : TK Lee

When program to print integers by increment by 1.
But don't print multiple of 3.

e.g) 1 2 4 5 7 8 10 11 13 14

Input :

Accept integers (1 ~ 100)

10

Expected Output :

Print integers but don't print multiple of 3

1 2 4 5 7 8 10

'''

maxNum = int(input())
start = 1

while (start <= maxNum):
    if(start % 3 != 0):
        print(start, end=" ")
    start += 1
