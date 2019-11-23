if __name__ == "__main__":
    FLAG = "CTF{numb3r5_f0r_3v3ry7h1n6}"
    ENCODING = "".join([f"{ord(x):03d}" for x in FLAG])
    
    with open("script.py", "w") as f:
        f.write('"' * 3)
        f.write("\nENCODING : A string that contains the ASCII encoding of the FLAG\n")
        f.write('"' * 3)
        f.write(f"""\nENCODING = "{ENCODING}"\n""")