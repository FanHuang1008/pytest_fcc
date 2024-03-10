import pytest
import source.my_functions as my_functions
import time


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_str():
    result = my_functions.add("I like ", "burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0)

@pytest.mark.slow
def test_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

@pytest.mark.skip(reason="This function is currently unavailable")
def test_add():
    result = my_functions.add(1, 3)
    assert result == 4

@pytest.mark.xfail(reason="We cannot divide by zero")
def test_broken():
    my_functions.divide(10, 0)