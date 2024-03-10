import pytest
import source.shapes as shapes
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.Circle = shapes.Circle(10)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.Circle
    
    def test_area(self):
        assert self.Circle.area() == self.Circle.radius ** 2 * math.pi
    
    def test_perimeter(self):
        assert self.Circle.perimeter() == self.Circle.radius * 2 * math.pi
    
    def test_circle(self, my_rectangle):
        assert self.Circle.area() != my_rectangle.area()