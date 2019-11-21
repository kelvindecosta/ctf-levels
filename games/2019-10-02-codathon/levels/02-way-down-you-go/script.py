def flag(i):                                                    # Returns a string (flag) given an integer (i)
    return "CTF{" + str(i) + "_r3cur510n5_p3rm1773d}"


def factorial(n):                                               # Returns the factorial of a number
    if n == 0:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    """
    You musn't be afraid to dream a little bigger, darling.
    
    ---

    When you find the number, use the 'flag' function to get the flag.
    """
    print(factorial(5))