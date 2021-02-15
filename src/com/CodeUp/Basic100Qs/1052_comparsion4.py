'''
Code Up - Algorithm Basic - 100 Questions

[기초-비교연산] 1052 comparison
https://codeup.kr/problem.php?id=1052

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two Integer

0 1

Expected Output :

If two integer is different print 1 otherwise print 0

1

'''

a, b = [int(x) for x in input().split()]
if b >= a:
    print(1)
else:
    print(0)
