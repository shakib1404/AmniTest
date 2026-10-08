# Calculator

A simple calculator module with basic arithmetic and temperature conversion functions.

## Functions

### divide(a, b)
Divides `a` by `b` and returns the result.

```python
from calculator import divide
result = divide(10, 2)  # Returns 5.0
```

### average(nums)
Calculates the average of a list of numbers.

```python
from calculator import average
result = average([1, 2, 3])  # Returns 2.0
```

Raises `ValueError` if the list is empty.

### celsius_to_fahrenheit(c)
Converts temperature from Celsius to Fahrenheit.

```python
from calculator import celsius_to_fahrenheit
result = celsius_to_fahrenheit(0)  # Returns 32.0
```

### fahrenheit_to_celsius(f)
Converts temperature from Fahrenheit to Celsius.

```python
from calculator import fahrenheit_to_celsius
result = fahrenheit_to_celsius(32)  # Returns 0.0
result = fahrenheit_to_celsius(212) # Returns 100.0
```

## Testing

Run tests with pytest:

```bash
pytest test_calculator.py -v
```
