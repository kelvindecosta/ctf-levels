import random
from itertools import permutations

def flag(x):
    return "CTF{" + str(x) +"}"

if __name__ == "__main__":
    base = "c4l0rd3u5"
    end = flag(base)
    n = 630

    random.seed(42)
    cases = [flag("".join(p)) for p in permutations(base)]
    random.shuffle(cases)
    
    DICTIONARY = {}

    while len(cases) > 0:
        ring = cases[:n]
        cases = cases[n:]

        if end in ring:
            ring[ring.index(end)] = ring[-1]
            ring[-1] = end
            DICTIONARY["flag"] = ring[0]
        
        for i in range(len(ring)-1):
            DICTIONARY[ring[i]] = ring[i+1]

    with open("script.py", "w") as f:
        f.write('"' * 3)
        f.write("\nDICTIONARY : A string\n")
        f.write('"' * 3)
        f.write(f"""\nDICTIONARY = {DICTIONARY}\n""")
