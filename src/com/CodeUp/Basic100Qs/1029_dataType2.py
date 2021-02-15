'''
Code Up - Algorithm Basic - 100 Questions

[기초-데이터형] 1029 Data Type - Print Float
https://codeup.kr/problem.php?id=1029

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive float (+- 1.7*10-308 ~ +- 1.7*10308 )

3.14159265359

Expected Output :

Print float variable

3.14159265359

'''

num = input()
print('%.11f' % float(num))
