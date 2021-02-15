'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1067 Conditional Loop - Nested Loop
https://codeup.kr/problem.php?id=1067

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 1 integer
(-2147483648 ~ +2147483647)

-2147483648

Expected Output :

Print minus or plus on the first line and print odd or even in second line.

minus
even

'''
a = int(input())

if (a > 0):
    print("plus")
    if (a % 2 == 0):
        print("even")
    else:
        print("odd")

else:
    print("minus")
    if (a % 2 == 0):
        print("even")
    else:
        print("odd")
