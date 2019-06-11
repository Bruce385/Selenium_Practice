val = 9


def test(flag):
    global val
    if flag:
        val = 1
    else:
        print(test)
    return val


if __name__ == '__main__':
    ret = test(0)
    print(ret)
