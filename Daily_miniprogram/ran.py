"""做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用python生成200个激活码"""

#直接使用python的UUID模块
import uuid as u
def rand_uuid():
    f = open('coupon.txt','w+')
    for i in range(200):
        ID = str(u.uuid1()) + '\n'
        f.write(ID)
    f.close()

if __name__ == '__main__':
    rand_uuid()
