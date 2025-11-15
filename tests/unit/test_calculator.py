import pytest
from calculator.library import Calculator

class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(-1, -1) == -2
        assert calc.add(0, 0) == 0
        assert calc.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(3, 2) == 1
        assert calc.subtract(-1, 1) == -2
        assert calc.subtract(-1, -1) == 0
        assert calc.subtract(0, 0) == 0
        assert calc.subtract(2.5, 1.5) == 1.0

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-1, 1) == -1
        assert calc.multiply(-1, -1) == 1
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(1.5, 2) == 3.0

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(6, 3) == 2
        assert calc.divide(-6, 3) == -2
        assert calc.divide(6, -3) == -2
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(0, 5) == 0

    def test_exponentiate(self):
        calc = Calculator()
        assert calc.exponentiate(2, 3) == 8
        assert calc.exponentiate(5, 0) == 1
        assert calc.exponentiate(10, 1) == 10
        assert calc.exponentiate(2, -1) == 0.5
        assert calc.exponentiate(4, 0.5) == 2.0

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_add_non_numeric_input(self):
        calc = Calculator()
        with pytest.raises(TypeError, match="Inputs must be numeric"):
            calc.add(1, "2")
        with pytest.raises(TypeError, match="Inputs must be numeric"):
            calc.add("1", 2)
        with pytest.raises(TypeError, match="Inputs must be numeric"):
            calc.add("1", "2")
