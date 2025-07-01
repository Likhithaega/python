# text = input("Enter a string: ")

# capitalized = ""

# for i in range(len(text)):
#     char = text[i]
#     # Convert only the first character if it's a lowercase letter
#     if i == 0 and 'a' <= char <= 'z':
#         capitalized += chr(ord(char) - 32)  # Convert to uppercase manually
#     elif i > 0 and 'A' <= char <= 'Z':
#         capitalized += chr(ord(char) + 32)  # Convert to lowercase manually
#     else:
#         capitalized += char  # Keep it as it is

# print("Capitalized string:", capitalized)
text = input("Enter a string: ")

words = text.split()
capitalized_words = [word.capitalize() for word in words]
result = " ".join(capitalized_words)

print("Capitalized string:", result)
