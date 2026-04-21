class ReverseString:
    def __init__(self, text):
        self.__text = text
    def get_reverse(self):
        return self.__text[::-1]
    def __str__(self):
        return self.get_reverse()
user_input = input("Enter a string: ")
obj = ReverseString(user_input)
print("Reversed string :", obj.get_reverse())
print("Reversed string:", obj)