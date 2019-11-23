"""
ENCODING : A string that contains the ASCII encoding of the FLAG
"""
ENCODING = "067084070123110117109098051114053095102048114095051118051114121055104049110054125"

if __name__ == "__main__":
    FLAG = "".join([chr(int(ENCODING[i:i+3])) for i in range(0, len(ENCODING), 3)])
    print(FLAG)