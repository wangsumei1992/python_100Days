import unittest

# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('foo'.isupper())
#
# if __name__ == "__main__":
#     unittest.main()
class PasswordTest(unittest.TestCase):

    def setUp(self):
        print('set up')
        self.test_data = [
            dict(name='jack', password='Iloverose'),
            dict(name='rose', password='Ilovejack'),
            dict(name='tom', password='password123')
        ]

    def test_weak_password(self):
        for data in self.test_data:
            passwd = data['password']

            self.assertTrue(len(passwd) >= 6)
            msg = "user %s has a weak password" %(data['name'])
            self.assertTrue(passwd != 'password123', msg= msg)
            self.assertTrue(passwd != 'password', msg= msg)

if __name__ == '__main__':
    unittest.main()
