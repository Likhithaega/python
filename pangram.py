text=set(input("Enter the string: ").lower())
alphabets=set('abcdefghijklmnopqrstuvwxyz')
if alphabets.issubset(text):
    print("pangram" )
else:
    print("not a pangram" )