'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1015 Input/Output - Print float with 2 decimal places
https://codeup.kr/problem.php?id=1015

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Input One float

1.59254

Expected Output :

Round variable and print with two decimal places

1.59

Approch : 
"%.2f" // .2 will round up number and print 2 decimal places

'''
f = float(input())
print("%.2f" % f)
