#import pytest
def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tseti"

class TestClass():
    def test_one(self):
        x = "this"
        assert 'h' in x
