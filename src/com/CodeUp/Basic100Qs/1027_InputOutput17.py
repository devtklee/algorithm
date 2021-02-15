'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1027 Input/Output - change date format
https://codeup.kr/problem.php?id=1027

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive date as yyyy.mm.dd format

2014.07.15

Expected Output :

print date as dd-mm-yyyy format

15-07-2014 

'''
y, m, d = input().split('.')
print(str(d) + '-' + str(m) + '-' + str(y))
