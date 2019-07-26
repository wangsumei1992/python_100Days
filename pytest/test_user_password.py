import pytest
import json

class TestUserPassword(object):
    @pytest.fixture()
    def users(self):
        #读取当前路径下的json文件，返回的结果是dict
        return json.loads(open('./users.dev.json', 'r').read())

    def test_user_password(self, users):
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password123', msg
            assert passwd != 'password', msg