# API Contract for the Calculator Library

from typing import Union

Numeric = Union[int, float]

class Calculator:
    """
    A class to perform basic arithmetic operations.
    """

    def add(self, a: Numeric, b: Numeric) -> Numeric:
        """
        Adds two numbers.
        """
        pass

    def subtract(self, a: Numeric, b: Numeric) -> Numeric:
        """
        Subtracts the second number from the first.
        """
        pass

    def multiply(self, a: Numeric, b: Numeric) -> Numeric:
        """
        Multiplies two numbers.
        """
        pass

    def divide(self, a: Numeric, b: Numeric) -> Numeric:
        """
        Divides the first number by the second.
        Raises:
            ValueError: If the divisor (b) is zero.
        """
        pass

    def exponentiate(self, base: Numeric, exp: Numeric) -> Numeric:
        """
        Raises the base to the power of the exponent.
        """
        pass
