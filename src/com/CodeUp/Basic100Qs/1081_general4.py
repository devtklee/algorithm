'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1081 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1081

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 2 integers (n, m) (n, m < 10)

2 3

Expected Output :

first number represent 

'''

n, m = input().split()

for i in range(1, int(n)+1):
    for j in range(1, int(m)+1):
        print(i, j)
