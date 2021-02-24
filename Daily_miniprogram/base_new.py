'''
age = 27
name = "zhangsan"
print("student info: %d %s." %(age,name))
'''
# 测试提交
# def f1(x):
#     print(x)
# def power(x,n):
#     '''位置参数'''
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# a = power(3, 2)
# print(a)
# def enroll(name, gender, age = 6):
#     '''默认参数'''
#     print(name)
# enroll("wangsumei", "女")
# print(help(enroll))
# def person(name, **kw):
#     print("name: %s, other: %s" %(name, kw) )
# #person('wanglele',city = "beijing",job = "engineer")
# ext = {'city': 'Beijing', 'job': 'Engineer'}
# person('wanglele',**ext)
# d = {'a':1,'b':2,'c':3}
# for key in d:
#     print(key)
# f = d.items()
# print(f)
#如何判断一个对象是不是可迭代对象
from collections import Iterable
f = isinstance(list(range(100)), Iterable)
print(f)


