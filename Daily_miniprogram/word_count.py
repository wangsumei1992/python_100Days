#任一个英文的纯文本文件，统计其中的单词出现的个数

import re
from collections import Counter

def cal(filename="test1.txt"):
    with open(filename, 'r') as f:
        data = f.read()
    data1 = data.lower()
    #替换了除了n't这类连字符串外的所有非单词字符和数字字符
    data_list = re.split(r'[\s\n]+', data1)
    return Counter(data_list).most_common()

if __name__ == "__main__":
    dic = cal()
    for i in range(len(dic)):
        print('%15s  ---->   %3s' % (dic[i][0],dic[i][1]))