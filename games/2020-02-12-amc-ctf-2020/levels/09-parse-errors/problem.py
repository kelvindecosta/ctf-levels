from random import randrange, choice, shuffle
from string import ascii_letters, digits
from os import path


if __name__ == "__main__":
    data = []
    flag = "CTF{wh47_700k_y0u_50_l0n6}"
    data.append(flag)

    for i in range(1, 10000):
        temp = list(flag)
        for j in range(0, randrange(1, 5)):
            temp[randrange(4, len(flag)-1)] = choice(ascii_letters + digits)
        for j in range(0, randrange(1, 4)):
            temp[randrange(4, len(flag)-1)] = choice("{}")
    
        data.append("".join(temp))
    
    shuffle(data)
    logfile = "logfile.txt"
    if not path.exists(logfile):
        with open(logfile, "w") as f:
            for n in data:
                f.write(n + "\n")