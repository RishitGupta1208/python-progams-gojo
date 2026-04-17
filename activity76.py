ui = input("Enter 4 numbers separated by space: ")
nums = tuple(map(int, ui.split()))

result = 1
for i in nums:
    result *= i

print("Multiplication:", result)