'''
Code Up - Algorithm Basic - 100 Questions

[기초-산술연산] 1042 Arithmetic - Division
https://codeup.kr/problem.php?id=1042  

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two integer

1 3

Expected Output :

Print only integer after diving two integer

0

'''

x, y = [int(i) for i in input().split()]
d = x/y
print('%d' % d)
