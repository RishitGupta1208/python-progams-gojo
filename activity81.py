num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
capitalized_fruits = [fruit.capitalize() for fruit in ["apple", "banana", "mango", "orange", "grape"]]
print("Odd numbers:", odd_numbers)
print("Capitalized fruits:", capitalized_fruits)