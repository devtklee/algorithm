'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1080 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1080

Date : 2021-02-15
Solved BY : TK Lee

Input :

Input 1 tenger

55

Expected Output :

add numbers from 1 until sum is equal or bigger than input value.
Print latest number used to add.

10

'''

start = 1
sum = 0
max = int(input())

while (max >= sum):
    sum += start
    if(sum < max):
        start += 1
    else:
        break

print(start)
