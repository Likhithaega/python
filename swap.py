text = input("Enter a string: ")
# swapped = text.swapcase()
# print("Swapped case string:", swapped)
swapped=""
for char in text:
    if (char.isupper()):
        swapped+=char.lower()
    elif(char.islower()):
        swapped+=char.upper()
    else:
        swapped+=char
print(swapped)
