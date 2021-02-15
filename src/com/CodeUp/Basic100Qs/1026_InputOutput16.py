'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1026 Input/Output - Split Time stamp
https://codeup.kr/problem.php?id=1026

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive hour, minutes, second as hh:mm:ss 

17:23:57

Expected Output :

print only minutes

23

'''

y, m, s = input().split(':')
print(int(m))
