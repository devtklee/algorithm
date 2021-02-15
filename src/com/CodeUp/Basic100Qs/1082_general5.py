'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1082 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1082

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 numbers in hexdecimal

B

Expected Output :

Print multiplification of inputed number from 1 to F

B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5

'''

h = input()

for i in range(1, 16):
    print("%X*%X=%X" % (int(h, 16), i, (int(h, 16) * i)))
