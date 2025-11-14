# Quickstart Guide: Calculator Library

This guide shows how to use the `Calculator` library.

## Installation

This library is a local module and does not require installation from a package manager. Ensure your Python environment is set up to see the `src` directory.

## Usage

Here is a basic example of how to use the `Calculator` class:

```python
from calculator.library import Calculator

# 1. Create an instance of the Calculator
calc = Calculator()

# 2. Perform operations
result_add = calc.add(10, 5)
print(f"10 + 5 = {result_add}")  # Output: 15

result_sub = calc.subtract(10, 5)
print(f"10 - 5 = {result_sub}")  # Output: 5

result_mul = calc.multiply(10, 5)
print(f"10 * 5 = {result_mul}")  # Output: 50

result_div = calc.divide(10, 5)
print(f"10 / 5 = {result_div}")  # Output: 2.0

result_exp = calc.exponentiate(2, 3)
print(f"2^3 = {result_exp}")  # Output: 8

# 3. Handle errors
try:
    calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Division by zero is not allowed.

try:
    calc.add(10, "a")
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: Invalid input type.
```
