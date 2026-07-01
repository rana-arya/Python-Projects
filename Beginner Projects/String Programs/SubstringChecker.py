# Arya Rana
#SubstringChecker.py

def TEST(string, sub):
    if sub in string:
        print("Substring exists in the string.")
    else:
        print("Substring does not exist in the string.")

main = input("Enter the main string: ")
sub = input("Enter the substring: ")
TEST(main, sub)

#OUTPUT:
#Enter the main string: computer
#Enter the substring: put
#Substring exists in the string.
