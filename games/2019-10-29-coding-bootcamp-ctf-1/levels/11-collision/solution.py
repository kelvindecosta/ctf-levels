"""
A : A list with 100 thousand unique strings
B : A list with 100 thousand unique strings
"""

if __name__ == "__main__":
    A = set(A)
    B = set(B)

    print((A & B).pop())
    