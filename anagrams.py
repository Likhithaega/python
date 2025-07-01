def anagram(text1,text2):
    if sorted(text1)==sorted(text2):
        return "anagrams"
    else:
        return "not anagrams"
text1=input("Enter the string 1: ")
text2=input("Enter the string 2: ")
print(anagram(text1,text2))