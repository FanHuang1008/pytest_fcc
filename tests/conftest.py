import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def his_rectangle():
    return shapes.Rectangle(5, 6)

@pytest.fixture
def her_rectangle():
    return shapes.Rectangle(10, 20)