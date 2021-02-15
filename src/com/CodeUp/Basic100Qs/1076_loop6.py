'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1075 Loop
https://codeup.kr/problem.php?id=1075

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 small character (a-z)

f

Expected Output :

print alphabet in order from a to inputed character

a b c d e f

'''

start = (ord('a'))
end = (ord(input()))

while (end >= start):
    print(chr(start), end=' ')
    start += 1
