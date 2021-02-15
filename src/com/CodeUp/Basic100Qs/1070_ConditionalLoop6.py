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


def calendar(m):
    swticher = {
        12 | 1 | 2: "winter",
        1: 12,
        (3, 4, 5): "spring",
        (6, 7, 8): "summer",
        (9, 10, 11): "fall",
    }
    return swticher.get(m, "unknown")


print(calendar(m))
