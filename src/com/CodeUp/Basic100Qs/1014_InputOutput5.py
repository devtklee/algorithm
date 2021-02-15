'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1014 Input/Output - Print Two Characters in different order
https://codeup.kr/problem.php?id=1014

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Two character will be entered seperated by spaces

A b

Expected Output :

print two characters by descending order

b A

Approch : 
x, y = input().split()
print(y,x) // print variable in descending order

'''
x, y = input().split()
print(y, x)
