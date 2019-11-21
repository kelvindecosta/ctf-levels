from os import path
import random
import string

if __name__ == "__main__":
    flag = "CTF{7w0_h0rcrux35}"
    p1 = str.encode("".join([random.choice(string.ascii_letters + string.digits) for _ in range(len(flag))]))
    flag = str.encode(flag)
    p2 = bytes(a ^ b for (a, b) in zip(p1, flag))
    
    with open("p1.txt", "wb") as f:
        f.write(p1)
    
    with open("p2.txt", "wb") as f:
        f.write(p2)