# Arya Rana
# TupleStringLengths.py
# Accepts 10 strings from the user, stores them in a tuple, and displays each string along with its length.

def TEST(t):
    for s in t:
        print(s, "length:", len(s))

t = ()
for i in range(10):
    s = input("Enter string: ")
    t = t + (s,)

TEST(t)

#OUTPUT:
#Enter string: hello
#Enter string: world
#Enter string: python
#... (10 strings)
#hello length: 5
#world length: 5
#python length: 6
