# Arya Rana
# WordCountFromFile.py
# Reads a text file and counts the total number of words using Python's file handling and string operations.

def TEST():
    f = open("story.txt", "r")
    text = f.read()
    f.close()
    words = text.split()
    print("Number of words:", len(words))

TEST()

#OUTPUT
#Number of words: 4
