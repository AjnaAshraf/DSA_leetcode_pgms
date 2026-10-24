scribbled_text = input("enter the scribbled text: ")
word  = input("enter word: ")


for ch in scribbled_text:

    if ch in word and scribbled_text.count(ch)<=word.count(ch):

        pass

    else :

        print("absent")
        break

else:

    print("present")
