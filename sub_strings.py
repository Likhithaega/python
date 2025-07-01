text= input("Enter the text: ")
length=len(text)
for i in range(length):
    for j in range(i+1,length+1):
        print(text[i:j])



