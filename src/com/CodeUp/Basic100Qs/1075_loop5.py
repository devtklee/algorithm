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

4
3
2
1
0

'''

start = int(input())

while start != 0:
    start -= 1
    print(start)
