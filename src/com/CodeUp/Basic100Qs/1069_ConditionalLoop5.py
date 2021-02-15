'''
Code Up - Algorithm Basic - 100 Questions

[기초-조건/선택실행구조] 1069 Conditional Loop - Switch Statement
https://codeup.kr/problem.php?id=1069

Date : 2021-02-14
Solved BY : TK Lee

Input : 

Receive 1 character
(A-Z)

A

Expected Output :

Print output based on the condition below : 
A : best!!!
B : good!!
C : run!
D : slowly~
else : what?

best!!!

'''
c = input()


def con(c):
    swticher = {
        'A': "best!!!",
        'B': "good!!",
        'C': "run!",
        'D': "slowly~"
    }
    return swticher.get(c, "what?")


print(con(c))
