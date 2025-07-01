text1=input("Enter the string 1: ")
text2=input("Enter the second string: ")
if len(text1)==len(text2) and (text2 in text1+text1):
    print("second string is rotation of first string")
else:
    print("second string is not rotation of first string")



