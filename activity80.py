data = {'Codingal':3, 'is':2, 'the':2, 'best':2, 'for':2, 'Coding':1}
word = input("Enter the word to check: ")
if word in data:
    print(f"'{word}' occurs {data[word]} times.")
else:
    print(f"'{word}' is not present in the dictionary.")