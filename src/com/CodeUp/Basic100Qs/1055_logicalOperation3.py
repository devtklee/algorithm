'''
Code Up - Algorithm Basic - 100 Questions

[기초-논리연산] 1055 Logical Operation
https://codeup.kr/problem.php?id=1055

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer (only 1 or 0)

1 1

Expected Output :

If any integer have 1, print 1. Otherwise 0

1

'''

a, b = [int(x) for x in input().split()]

if (a | b) == 1:
    print(1)
else:
    print(0)
