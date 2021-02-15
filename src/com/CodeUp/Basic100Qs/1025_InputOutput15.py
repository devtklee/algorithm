'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1025 Input/Output - Split Integer
https://codeup.kr/problem.php?id=1025

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive integer with 5 digits

75254

Expected Output :

print each digits in seperated line within [] square bracket

[70000]
[5000]
[200]
[50]
[4]

'''
num = str(input())

idx = 0
numrange = len(num)
maxcnt = numrange-1

while idx < numrange:
    print('[' + str(int(num[idx]) * (pow(10, maxcnt))) + ']')
    idx += 1
    maxcnt -= 1
