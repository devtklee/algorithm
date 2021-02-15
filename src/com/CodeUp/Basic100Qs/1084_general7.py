'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1084 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1084

Date : 2021-02-15
Solved BY : TK Lee

Input :

accept r, g, b color weight (0-128) by spaces

2 2 2

Expected Output :

print all the possible combinations of r, g, b count 
Print number of possiblities in the last line.

0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8

'''

r, g, b = [int(n) for n in input().split()]
cnt = 0

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            cnt += 1

print(cnt)
