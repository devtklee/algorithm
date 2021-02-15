'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1070 Conditional Loop - Switch Statement
https://codeup.kr/problem.php?id=1070

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 1 Integer that represent month (1-12)

12

Expected Output :

Print output based on the condition below : 
12, 1, 2   : winter
 3, 4, 5   : spring
 6, 7, 8   : summer
9, 10, 11  : fall

winter

'''
m = int(input())

if (m == 12 or m == 1 or m == 2):
    print("winter")
elif (m >= 3 and m < 6):
    print("spring")
elif (m >= 6 and m < 9):
    print("summer")
elif (m >= 9 and m < 12):
    print("fall")
