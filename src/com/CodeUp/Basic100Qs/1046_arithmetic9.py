'''
Code Up - Algorithm Basic - 100 Questions

[기초-산술연산] 1046 Arithmetic - Sum, Average
https://codeup.kr/problem.php?id=1046

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive Three Integer

1 2 3

Expected Output :

Print Sum of 3 integer and average by each line

6
2.0

'''

x, y, z = [int(n) for n in input().split()]

s = x+y+z
a = s/3

print("%d" % s)
print("%.1f" % a)
