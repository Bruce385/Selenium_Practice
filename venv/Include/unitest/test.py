from calculator import Count


class TestCount:
    def test_add(self):
        try:
            a = int(input('请输入a:'))
            b = int(input('请输入b:'))
        except ValueError:
            print('请输入准确的整数')
        else:
            try:
                j = Count(a, b)
                assert (j.add() == 9), 'not pass'
            except AssertionError as msg:
                print(msg)
            else:
                print('Test pass!')


mytest = TestCount()
mytest.test_add()
