import calc


def test_add():
    if calc.add(5, 7) == 12:
        print('test ADD is OK')
    else:
        print('test ADD is FAIL')


def test_sub():
    if calc.sub(13, 9) == 4:
        print('test SUB is OK')
    else:
        print('test SUB is FAIL')


def test_mul():
    if calc.mul(5, 8) == 40:
        print('test MUL is OK')
    else:
        print('test MUL is FAIL')


def test_div():
    if calc.div(90, 10) == 9:
        print('test DIV is OK')
    else:
        print('test DIV is FAIL')


test_add()
test_sub()
test_mul()
test_div()