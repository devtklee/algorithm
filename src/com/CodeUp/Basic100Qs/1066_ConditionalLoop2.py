'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1066 Conditional Loop
https://codeup.kr/problem.php?id=1066

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 3 integer
(-2147483648 ~ +2147483647)

1 2 8

Expected Output :

Print even numbers in seperated line

odd
even
even

'''
a, b, c = [int(x) for x in input().split()]

if (a % 2 == 0):
    print("even")
else:
    print("odd")

if (b % 2 == 0):
    print("even")
else:
    print("odd")

if (c % 2 == 0):
    print("even")
else:
    print("odd")
