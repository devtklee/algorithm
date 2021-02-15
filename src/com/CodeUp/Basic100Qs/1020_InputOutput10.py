'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1020 Input/Output - Replace character
https://codeup.kr/problem.php?id=1020

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Receive String with Hyphen

000907-1121112

Expected Output :

Remove hyphen and print string

0009071121112

Approach :

use replace() function to replace specific character.

'''

sin = input()
print(sin.replace('-', ''))
