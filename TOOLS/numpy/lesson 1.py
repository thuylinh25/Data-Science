# # # -- coding: utf8 --
import numpy as np
import math
from math import sqrt
1/ Viết chương trình xuất ra màn hình hình vuông đặc kí tự "*" có cạnh bằng a (với a nhập từ bàn phím).
import numpy as np
a = int(input("Nhap so a: "))
A=np.full((a,a),"*")
print(A)

# 2/ Viết chương trình nhập vào ba cạnh của một tam giác, tính và xuất ra diện tích của tam giác đó.

import math
from math import sqrt
a = int(input("Nhap vao canh a:"))
b = int(input("Nhap vao canh b: "))
c = int(input("Nhap vao canh c: "))
if (a+b>c) & (b+c>a) & (a+c>b) & (a>0) & (b>0) & (c>0):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Dien tich tam giac bang {area}")
else:
    print("Khong tao thanh tam giac")

# 3/Viết chương trình tính n!! với n!! = 1.3.5...n nếu n lẻ, n!! = 2.4.6...n nếu n chẵn.
n = int(input("Moi nhap so nguyen duong n:"))
factorial_n = 1
if n % 2 == 0:
    list_n = np.arange(2,n,2)
    print(list_n)
else:
    list_n = np.arange(1,n,2)
    print(list_n)
for i in list_n:
    factorial_n *=i
print(f"n!! = {factorial_n}")

# 4/Viết chương trình giải phương trình bậc 2 với các hệ số nhập từ bàn phím (xét đầy đủ các trường hợp)
from math import sqrt
def giaiPTBac2(a, b, c):
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ", + (-c / b))
        return

    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
    elif delta == 0:
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
    else:
        print("Phương trình vô nghiệm!")

a = float(input("Nhập hệ số bậc 2, a = "))
b = float(input("Nhập hệ số bậc 1, b = "))
c = float(input("Nhập hằng số tự do, c = "))

giaiPTBac2(a, b, c)

# 5/Viết chương trình tính số Fibonashi thứ n.
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
n =(int(input("nhap n:")))
print (fib(n))
# 6/ Cho mảng một chiều các số thực hãy tìm đoạn [a,b] sao cho đoạn này chứa tất cả các giá trị trong mảng (a,b: số nguyên). (Sử dụng numpy)
A = np.array([1.3, 5.9,9.6,5.5])
A = np.round(A)
a = int(min(A))
b = int(max(A))
print(f"Doan [{a},{b}] chua tat ca cac gia tri trong mang")
