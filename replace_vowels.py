text= input("Enter the string: ")
vowels="AEIOUaeiou"
for char in text:
    if char in vowels:
        text=text.replace(char,"*")
print(text)