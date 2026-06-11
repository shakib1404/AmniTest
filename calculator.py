def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def average(nums):
    if not nums:
        raise ValueError("Cannot calculate average of empty list")
    return sum(nums) / len(nums)

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == "__main__":
    print(divide(10, 2))
    print(average([1, 2, 3]))
