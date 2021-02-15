'''
Code Up - Algorithm Basic - 100 Questions

[기초-비교연산] 1050 comparison
https://codeup.kr/problem.php?id=1050

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two Integer

0 0

Expected Output :

if two integer is same, print 1
Otherwise print 0

1

'''

a, b = [int(x) for x in input().split()]
if a == b:
    print(1)
else:
    print(0)
