print("---------TEXT ANALYZER----------")
text = input("Enter your text here: ")
chars = len(text)
words = text.split()
counting = len(words)
vowels = 0
spaces = 0
for char in text:
    if char.lower() in "aeiou":
        vowels = vowels+1
    if char ==" ":
        spaces = spaces+1
print("--------RESULT---------")
print(f"Text: {text}")
print(f"Characters: {chars}")
print(f"Vowels: {vowels}")
print(f"Spaces: {spaces}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Reverse: {text[::-1]}")
