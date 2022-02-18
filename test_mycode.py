from mycode import Example
import numpy as np


def test_hello():
    c = Example()
    text = "Dew"
    c.hello(text)


def test_numpy():
    x = [1, 3, 2]
    output = int(np.max(x))
    assert output == 3
