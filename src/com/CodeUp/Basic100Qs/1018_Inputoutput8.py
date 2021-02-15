'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1018 Input/Output - Print Time
https://codeup.kr/problem.php?id=1018

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Hour and Minutes seperated by ":" colon.

3:16

Expected Output :

Print received time as Hour:Mintues

3:16

'''

h, m = input().split(":")
print("%s:%s" % (h, m))
