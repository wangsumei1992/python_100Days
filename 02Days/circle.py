"""输入半径计算圆的周长与面积"""
import math

radius = float(input("请输入圆的半径:"))
perimeter = math.pi * radius * 2
area = math.pi * radius * radius
print('周长: %.2f' % (perimeter))
print('面积: %.2f' % (area))