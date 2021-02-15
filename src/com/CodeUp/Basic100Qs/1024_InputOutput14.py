'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1024 Input/Output - Split characters
https://codeup.kr/problem.php?id=1024

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Receive Word

Boy

Expected Output :

Split each characters by seperated line with single quote

'B'
'o'
'y'

'''

word = input()
for c in word:
    print("\'"+c+"\'")
