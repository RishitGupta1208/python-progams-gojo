num = int(input("Enter a number: "))
binary = ""

while num > 0:
    temp = ""
    
    for i in range(1):
        remainder = num % 2
        temp = str(remainder)
    
    binary = temp + binary
    num = num // 2

print("Binary equivalent:", binary)