'''
Code Up - Algorithm Basic - 100 Questions

[기초-비트단위논리연산] 1062 Bitwise Logical Operation
https://codeup.kr/problem.php?id=1062

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive integer
(-2147483648 ~ +2147483647)

3 5

Expected Output :

Calculatetwo integers bitwise "XOR" logical operation & output as decimal number.

6

'''

a, b = [int(x) for x in input().split()]

c = a ^ b
print(c)
