from mycode import Example
import numpy as np


def test_hello():
    c = Example()
    text = "Dew"
    c.hello(text)


def test_numpy():
    x = [1, 3, 5]
    output = np.max(x)
    assert output == 3
