'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1065 Conditional Loop
https://codeup.kr/problem.php?id=1065

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 3 integer
(-2147483648 ~ +2147483647)

1 2 4

Expected Output :

Print even numbers in seperated line

2
4

'''
a, b, c = [int(x) for x in input().split()]

if (a % 2 == 0):
    print(a)

if (b % 2 == 0):
    print(b)

if (c % 2 == 0):
    print(c)
