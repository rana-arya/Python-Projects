# Arya Rana
# QuotientAndRemainder.py
# Calculates the quotient and remainder of two integers using integer division and handles division by zero using exception handling.

def TEST(a, b):
    try:
        q = a // b
        r = a % b
        print("Quotient:", q)
        print("Remainder:", r)
    except:
        print("Division by zero not allowed!")

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
TEST(a, b)

#OUTPUT:
#Enter numerator: 10
#Enter denominator: 3
#Quotient: 3
#Remainder: 1
