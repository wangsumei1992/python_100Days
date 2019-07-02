"""运算符的使用"""
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a=",a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1=", flag1)
print("flag2=", flag2)
print("flag3=", flag3)
print("flag4=", flag4)
print("flag5=", flag5)

str1 = 'hello, world!'
print('字符串的长度是:',len(str1))
print('单词首字母大写:',str1.title())
print('字符串变大写:',str1.upper())
print('字符串是不是以hello开头:',str1.startswith('hello'))