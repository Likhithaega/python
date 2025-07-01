# text=input("Enter the string: ")
# most_repeated=""
# count=0
# for char in text.replace(" ",""):
#     if text.count(char) > count:
#         most_repeated=char
#         count=text.count(char)
# print(most_repeated)
from collections import Counter

text = input("Enter a string: ").replace(" ", "")
counter = Counter(text)

max_freq = max(counter.values())
most_frequent = [char for char, freq in counter.items() if freq == max_freq]

print(f"Most frequent character(s): {most_frequent}")
print(f"Frequency: {max_freq}")

