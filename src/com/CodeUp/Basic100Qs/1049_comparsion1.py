'''
Code Up - Algorithm Basic - 100 Questions

[기초-비교연산] 1049 comparison
https://codeup.kr/problem.php?id=1049

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive two Integer

9 1  

Expected Output :

if a larger b then 1 otherwise print 0
(First input : a, Second Input : b)

1

'''

a, b = [int(x) for x in input().split()]
if a > b:
    print(1)
else:
    print(0)
