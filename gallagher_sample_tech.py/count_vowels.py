text = input("Enter text: ").lower()
count =0 
vowels="aeiou"

for ch in text:

    if ch in vowels:

        count=count+1

print(count)
