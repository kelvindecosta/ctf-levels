from hashlib import md5

def flag(i):
    return "CTF{bru7u5_574bb3d_c4354r_" + str(i) + "_71m35}"


if __name__ == "__main__":
    """
    Et tu, Brute?

    ---

    Find the first positive integer for which the MD5 digest (hexadecimal) starts with 6 zeros
    """

    i = 0
    while True:
        bytelist = md5(str.encode(flag(i))).digest()[0:3]
        if all([ b == 0 for b in bytelist]):
            print(flag(i))
            break
        i += 1
