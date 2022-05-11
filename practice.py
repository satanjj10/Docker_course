#如何使用數字、數字的用法
from cmath import sqrt
from math import ceil, floor
from sqlite3 import sqlite_version_info


print(77)
print(8+5)
#整數除法
print(8//5)
#取餘數
print(8%5)
#str函式(只能印出來不能做相加)
number = -8
print("會印出數字" + str(number))
print(str(number) + str(number))
#abs取絕對值
print(abs(number))
#pow次方(2的0次方)
print(pow(2,0))
#max取最大值min取最小值 
print(max(2,3,88,100))
print(min(2,3,88,100))
#round四捨五入
print(round(4.4))
#from math import *(模組引入)
#floor無條件捨去，ceil無條件進位，sqrt開根號
print(floor(4.6))
print(ceil(5.1))
print(sqrt(36))
print('啦啦啦')
