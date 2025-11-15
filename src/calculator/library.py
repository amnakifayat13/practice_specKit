class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    Supports addition, subtraction, multiplication, division, and exponentiation
    for numeric inputs (integers and floats).
    """

    def _check_numeric(self, *args):
        """
        Internal helper method to validate if all provided arguments are numeric.

        Args:
            *args: Variable length argument list of inputs to check.

        Raises:
            TypeError: If any of the inputs are not an instance of int or float.
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Inputs must be numeric")

    def add(self, a, b):
        """
        Adds two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.

        Raises:
            TypeError: If either a or b is not numeric.
        """
        self._check_numeric(a, b)
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Args:
            a (int or float): The number to subtract from.
            b (int or float): The number to subtract.

        Returns:
            int or float: The difference between a and b.

        Raises:
            TypeError: If either a or b is not numeric.
        """
        self._check_numeric(a, b)
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.

        Raises:
            TypeError: If either a or b is not numeric.
        """
        self._check_numeric(a, b)
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second.

        Args:
            a (int or float): The numerator.
            b (int or float): The denominator.

        Returns:
            int or float: The quotient of a divided by b.

        Raises:
            TypeError: If either a or b is not numeric.
            ValueError: If the denominator b is zero.
        """
        self._check_numeric(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def exponentiate(self, base, exp):
        """
        Raises the base to the power of the exponent.

        Args:
            base (int or float): The base number.
            exp (int or float): The exponent.

        Returns:
            int or float: The result of base raised to the power of exp.

        Raises:
            TypeError: If either base or exp is not numeric.
        """
        self._check_numeric(base, exp)
        return base ** exp
