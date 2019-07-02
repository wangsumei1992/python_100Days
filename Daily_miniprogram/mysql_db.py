
#
# #连接数据库
# conn = connect(host='127.0.0.1',
#                user='root',
#                password='123456',
#                db = 'guest',
#                charset='utf8mb4',
#                cursorclass=cursors.DictCursor
#                )
# with conn.cursor() as cursor:
#     sql = 'select * from sign_guest'
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     # result1 = cursor.fetchall()
#     print(result)
# conn.commit()
# conn.close()
import random
import string
from pymysql import cursors, connect
import pymongo

#生成200个激活码
def create_code():
    code_list = list()
    for j in range(0,200):
        code_num = ''
        for i in range(0,15):
            n = random.choice(string.ascii_letters + '1234567890')
            code_num += n
        code_list.append(code_num)
    return code_list

code_list = create_code()
#print(code_list)
#储存到关系型数据库mysql
conn = connect(host='127.0.0.1',
                       user='root',
                       password='123456',
                       db='actcode',
                       charset='utf8mb4',
                       cursorclass=cursors.DictCursor
                       )
cursor = conn.cursor()
for code in code_list:
    sql = 'INSERT INTO code (code_content) values (\'{}\')'.format(code)
    cursor.execute(sql)
conn.commit()
conn.close()

#200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
conn = pymongo.MongoClient('localhost', 27017)
db = conn['test']
code= db['code']
for code_num in code_list:
    db.code.insert({'code': code_num})