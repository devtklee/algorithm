'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1013 Input/Output - two integer
https://codeup.kr/problem.php?id=1013

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Two integer will be entered seperated by spaces

1 2

Expected Output :

print two integers seperated by space

1 2

Approch : 
x, y = [int(i) for i in input().split()] // Receive input as integer type seperated by space
print("%d %d" % (x, y)) // print x, y as integer type

'''
x, y = [int(i) for i in input().split()]
print("%d %d" % (x, y))
