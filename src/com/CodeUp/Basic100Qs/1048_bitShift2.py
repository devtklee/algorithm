'''
Code Up - Algorithm Basic - 100 Questions

[기초-비트시프트연산] 1048 Bit Shifting 
https://codeup.kr/problem.php?id=1048

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two Integer (base, exponent)

1 3

Expected Output :

a * 2^b

8

'''

a, b = [int(x) for x in input().split()]
c = pow(2, b)
print(a*c)
