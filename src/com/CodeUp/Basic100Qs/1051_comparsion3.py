'''
Code Up - Algorithm Basic - 100 Questions

[기초-비교연산] 1051 comparison
https://codeup.kr/problem.php?id=1051

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two Integer

0 -1

Expected Output :

if b is bigger than a print 1 otherwise print 0

(First input : a, Second Input : b)

0

'''

a, b = [int(x) for x in input().split()]
if b >= a:
    print(1)
else:
    print(0)
