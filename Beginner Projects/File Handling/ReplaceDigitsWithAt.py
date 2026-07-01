# Arya Rana
# ReplaceDigitsWithAt.py
# Reads a text file, counts the number of digits, replaces each digit with @, and displays the modified text.

def TEST():
    f = open("story.txt", "r")
    text = f.read()
    f.close()
    digits = 0
    for ch in text:
        if ch.isdigit():
            digits += 1
    new_text = ""
    for ch in text:
        if ch.isdigit():
            new_text += "@"
        else:
            new_text += ch
    print("Digits:", digits)
    print("Modified text:\n", new_text)

TEST()

#OUTPUT
#Digits: 4
#Modified text:
#My age is @@ and my roll is @
