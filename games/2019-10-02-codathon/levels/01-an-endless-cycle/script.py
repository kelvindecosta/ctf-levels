from hashlib import sha256

def flag(i):                                            # Returns a string (flag) given an integer (i)
    return "CTF{br34k_7h3_l00p_" + str(i) + "_71m35}"


if __name__ == "__main__":
    """
    The question isn’t how, it’s when.

    ---

    Try running the script.
    """
    i = 0                                               # iterable
    best = None                                         # variable to hold the best value
    index = None                                        # variable to hold index which gives the best value

    while i < 256:
        cur = sha256(str.encode(flag(i))).hexdigest()   # gets some value, depending on 'i'
        if best is None or best < cur:                  # loop keeps checking for the best one
            best = cur
            index = i
        i += 1
        i %= 256
    
    print(flag(index))                                  # prints flag
