# text=input("Enter the string: ")
# vowels=["A","E","I","O","U","a","e","i","o","u"]
# v,c=0,0
# for char in text:
#     if char in vowels:
#         v+=1
#     else:
#         c+=1
# print(c,v)

vowels = "AEIOUaeiou"
v = c = 0

while (text := input("Enter the string (or 'quit' to exit): ")) != "quit":
    for char in text:
        (v := v + 1) if char in vowels else (c := c + 1)
    print(f"Consonants: {c}, Vowels: {v}")
