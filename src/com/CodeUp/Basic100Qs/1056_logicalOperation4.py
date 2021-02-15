'''
Code Up - Algorithm Basic - 100 Questions

[기초-논리연산] 1056 Logical Operation
https://codeup.kr/problem.php?id=1056

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer (only 1 or 0)

1 1

Expected Output :

If two integer is different print 1 otherwise 0

0

'''

a, b = [int(x) for x in input().split()]

if a != b:
    print(1)
else:
    print(0)
