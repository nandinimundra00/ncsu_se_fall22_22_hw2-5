from src.Num import Num
from src.main import oo
the={'nums':512}

def test_num():
    num = Num()
    for i in range(1, 101):
        num.add(i)
    mid, div = num.mid(), num.div()
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1, 1000):
        num.add(i)
    oo(num.nums())
    return 32 == len(num._has)