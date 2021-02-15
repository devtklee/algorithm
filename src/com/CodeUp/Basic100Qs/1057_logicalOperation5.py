'''
Code Up - Algorithm Basic - 100 Questions

[기초-논리연산] 1057 Logical Operation
https://codeup.kr/problem.php?id=1057

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer (only 1 or 0)

0 0

Expected Output :

If two integer is same print 1 otherwise 0

1

'''

a, b = [int(x) for x in input().split()]

if a != b:
    print(1)
else:
    print(0)
