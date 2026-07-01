# Arya Rana
# CountLinesStartingWithThe.py
# Reads a text file and counts the number of lines that start with the word "the" (case-insensitive).

def TEST():
    count = 0
    f = open("story.txt", "r")
    for line in f:
        if line.lower().startswith("the"):
            count += 1
    f.close()
    print("Number of sentences beginning with 'the':", count)

TEST()

#OUTPUT
#Number of sentences beginning with 'the': 2
