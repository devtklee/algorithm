'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1079 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1079

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept characters until 'q' is entered

x b k d l q g a c

Expected Output :

print characters in seperated line until 'q' is entered

x
b
k
d
l
q

'''

characters = input().split()

for c in characters:
    print(c)
    if (c == 'q'):
        break
