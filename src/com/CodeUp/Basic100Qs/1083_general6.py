'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1083 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1083

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 integer (1-9)

9

Expected Output :

Print numbers from 1 to received integer with spaces.
However if number is equal to 3, 6, or 9, print Captial 'X'

1 2 X 4 5 X 7 8 X

'''

end = int(input())

for n in range(1, (end+1)):
    if (n == 3 or n == 6 or n == 9):
        print('X', end=' ')
    else:
        print(n, end=' ')
