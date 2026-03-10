#5. Remove All Vowels from String

text = input("Enter string: ")

result = ""

for ch in text:
    if ch.lower() not in "aeiou":
        result += ch

print("Without vowels:", result)