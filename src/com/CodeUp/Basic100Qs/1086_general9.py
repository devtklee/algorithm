'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1086 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1086

Date : 2021-02-15
Solved BY : TK Lee

Even when images are stored on a computer, they are stored as digital data.

The most basic method is to change the color of one point (pixel) that composes the picture.
It converts and stores three light intensity values ​​separately: red (r), green (g), and blue (b).

For example, if you use 8 bits (0~255, 256 possible) for each color of r, g, b,

The color of one dot is represented by a total of 24 bits with 8 bits + 8 bits + 8 bits of 3 types of r, g, and b.
A total of 2^24 different light colors can be used.

It is possible to save one large image by collecting the points that are saved like that.
If you save as 24 bits for each dot in 1024 * 768 size,
You can calculate the storage capacity.

This is a typical image file that saves the raw data of the image as it is without compression.
It is a *.bmp file, and it is called bitmap method or raster method because it composes a picture with bits.

Given the image's horizontal resolution w, vertical resolution h, and bit b for storing one pixel,
Let's write a program that calculates the amount of storage required to store without compression.


E.g
For each point of the general 1024 * 768 size (resolution)
To store in 24 bits (3 pieces of 8 bits each in rgb), a storage capacity of 1024 * 768 * 24 bits is required.

If you want to check if it is, you can check it with a simple picture editing/editing program.


**
      8 bit(bit) = 1byte(byte) // 8bit=1Byte
1024 Byte(210 byte) = 1KB(Kilobyte) // 1024bit=1KB
1024 KB (210 KB) = 1 MB (megabytes)
1024 MB (210 MB) = 1 GB (gigabyte)
1024 GB (210 GB) = 1 TB (terabytes)

Input :

Accept w, h, b as integer
(w, h is integer (1~1024)
b <= 40 b is mulitpl of 4)

1024 768 24

Expected Output :

Print required spaces as MB unit.
(Round upto 2 decimal places )

2.25 MB

'''

w, h, b = [int(n) for n in input().split()]
u = "MB"

r = (((w*h*b) / pow(1024, 2))/8)
print("%.2f %s" % (r, u))
