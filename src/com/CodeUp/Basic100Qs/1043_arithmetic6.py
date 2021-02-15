'''
Code Up - Algorithm Basic - 100 Questions

[기초-산술연산] 1043 Arithmetic - Division
https://codeup.kr/problem.php?id=1043 

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer

10 3

Expected Output :

Print only reminder after diving two integer

1

'''

x, y = [int(i) for i in input().split()]
d = x % y
print('%d' % d)
