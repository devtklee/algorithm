'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1074 Loop
https://codeup.kr/problem.php?id=1074

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 integer (1-100)

5

Expected Output :

Count down input numbers until number = 1

5
4
3
2
1

'''

start = int(input())

while start != 0:
    print(start)
    start -= 1
