'''
Code Up - Algorithm Basic - 100 Questions

[기초-비트단위논리연산] 1059 Bitwise Logical Operation
https://codeup.kr/problem.php?id=1059

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive integer
(-2147483648 ~ +2147483647)

2

Expected Output :

Convert 1->0 0>1 in bit and print in decimal

-3

'''

a = int(input())

a = ~a
print(a)
