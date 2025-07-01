def alpha_numeric(text):
    for char in text:
        if not (char.isalnum()):
            return False
    return True
text= input("Enter the string: ").replace(" ","")
print(alpha_numeric(text))
    
