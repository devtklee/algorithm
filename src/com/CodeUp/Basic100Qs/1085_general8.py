'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1085 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1085

Date : 2021-02-15
Solved BY : TK Lee

When sound is stored in a computer, it is stored as digital data.

Through the microphone, the intensity of the sound is checked tens of times as little as tens of thousands of times per second.
You can convert the value to an integer value, save the value, and save the sound as a file.

When storing values, you can determine the degree of detailed recording according to the degree of use of the beat,
Saved in left and right (stereo) channels doubles… 5.1 channels require 6 times more storage space,
Longer recording times require more storage space.

H is the number of checking the sound strength and weakness of the microphone for 1 second.
(Hertz, Hz means how many times per second?

Bit b storing the result of one check
(If you use 2 bits, there are 0 or 1, and if you use 16 bits, there are 65536..)

Channel c, which is the number of tracks to store left and right sounds
(Mono means 1, stereo means 2 tracks.)

Given the time s to record,

Let's write a program that calculates the required storage capacity.

Actually, if you want to save for 1 second with normal CD sound quality (44.1KHz, 16bit, stereo)
44100 * 16 * 2 * 1 bit of storage space is required.

This recording method is called PCM (Pulse Code Modulation) method.
Uncompressed raw sound data files are typically *.wav.

Input :

accept h,b,c,s as integer
(   h <= 48,000
    b <= 32 but, b need to be multiple of 8
    c <= 5
    s <= 6000 )


44100 16 2 10

Expected Output :

Print required spaces as MB unit.
(Round upto 1 decimal places )

1.7 MB

'''

h, b, c, s = [int(n) for n in input().split()]
u = "MB"

r = (((h*b*c*s) / pow(1024, 2))/8)
print("%.1f %s" % (r, u))
