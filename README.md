# Calculator Project

A simple Python calculator module with basic arithmetic operations.

## Features

- **divide(a, b)**: Divides two numbers. Raises `ZeroDivisionError` if the divisor is zero.
- **average(nums)**: Calculates the average of a list of numbers. Raises `ValueError` if the list is empty.
- **celsius_to_fahrenheit(c)**: Converts temperature from Celsius to Fahrenheit.

## Usage

```python
from calculator import divide, average, celsius_to_fahrenheit

# Division
result = divide(10, 2)  # Returns 5.0

# Average
result = average([1, 2, 3])  # Returns 2.0

# Temperature conversion
result = celsius_to_fahrenheit(0)  # Returns 32.0
```

## Error Handling

- `divide(10, 0)` will raise `ZeroDivisionError`
- `average([])` will raise `ValueError`

## Testing

Run the test suite with pytest:

```bash
pytest test_calculator.py
```

## License

MIT
