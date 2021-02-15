'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1068 Conditional Loop
https://codeup.kr/problem.php?id=1068

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 1 integer
(0 ~ 100)

73

Expected Output :

Print output based on the condition below : 
90 - 100 : A
70 - 89  : B
40 - 69  : C
 0 - 39  : D

B

'''
a = int(input())

if (a >= 90):
    print("A")
elif (a >= 70):
    print("B")
elif (a >= 40):
    print("C")
else:
    print("D")
