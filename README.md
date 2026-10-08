# Calculator

A simple calculator module with basic arithmetic and temperature conversion functions.

## Functions

### divide(a, b)
Divides two numbers and returns the result as a float.

**Parameters:**
- `a`: The dividend (numeric)
- `b`: The divisor (numeric)

**Returns:** float - The result of a/b

**Raises:** ZeroDivisionError if b is 0

**Example:**
```python
from calculator import divide
result = divide(10, 2)  # Returns 5.0
```

### average(nums)
Calculates the average of a list of numbers.

**Parameters:**
- `nums`: A list of numeric values

**Returns:** float - The average of the numbers

**Raises:** ValueError if the list is empty

**Example:**
```python
from calculator import average
result = average([1, 2, 3])  # Returns 2.0
```

### celsius_to_fahrenheit(c)
Converts temperature from Celsius to Fahrenheit.

**Parameters:**
- `c`: Temperature in Celsius (numeric)

**Returns:** float - Temperature in Fahrenheit

**Formula:** F = C × 9/5 + 32

**Example:**
```python
from calculator import celsius_to_fahrenheit
result = celsius_to_fahrenheit(0)  # Returns 32.0
```

### fahrenheit_to_celsius(f)
Converts temperature from Fahrenheit to Celsius.

**Parameters:**
- `f`: Temperature in Fahrenheit (numeric)

**Returns:** float - Temperature in Celsius

**Formula:** C = (F - 32) × 5/9

**Example:**
```python
from calculator import fahrenheit_to_celsius
result = fahrenheit_to_celsius(32)  # Returns 0.0
result = fahrenheit_to_celsius(212)  # Returns 100.0
```
