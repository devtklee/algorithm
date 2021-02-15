'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1090 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1090

Date : 2021-02-15
Solved BY : TK Lee

The sequence of numbers according to a certain rule is called a sequence.

E.g
2 6 18 54 162 486 ... 
It starts from 2 and multiplies the previous number by 3 to create the next number.

In mathematics, this is said to be the same
It is said to be a sequence of geometric ratio (the Chinese word for the ratio is the same).


Youngil, who learned of the geometric sequence, suddenly became curious.

"Then.... What is the 13th number?"

Youngil wanted to create a program to automatically calculate a larger number.


When the starting value (a), the geometric ratio (r), and an integer (n) indicating the number of times are entered
Let's write a program that prints the nth number.

Input :

Accept starting value (a), difference (d), nth number (n) as integer (0 ~ 100)

2 3 7

Expected Output :

Print value of nth number in series

1458

'''

a, d, n = [int(i) for i in input().split()]
print(a * pow(d, (n-1)))
