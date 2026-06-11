def divide(a, b):
    return a / b          # BUG: crashes on b=0

def average(nums):
    return sum(nums) / len(nums)   # BUG: crashes on empty list

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == "__main__":
    print(divide(10, 2))
    print(average([1, 2, 3]))

