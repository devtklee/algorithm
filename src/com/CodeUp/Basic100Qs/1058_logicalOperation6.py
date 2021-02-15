'''
Code Up - Algorithm Basic - 100 Questions

[기초-논리연산] 1058 Logical Operation
https://codeup.kr/problem.php?id=1058

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer (only 1 or 0)

0 1

Expected Output :

If both integers are 0 print 1 otherwise 0

0

'''

a, b = [int(x) for x in input().split()]

if a == 0 and b == 0:
    print(1)
else:
    print(0)
