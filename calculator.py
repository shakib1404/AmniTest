def divide(a, b):
    return a / b          # BUG: crashes on b=0

def average(nums):
    if len(nums) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(nums) / len(nums)

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == "__main__":
    print(divide(10, 2))
    print(average([1, 2, 3]))

