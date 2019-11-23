import random
import string

def flag(x):
    return "CTF{" + str(x) +"}"

def random_string(l):
    charset = string.ascii_lowercase + string.digits
    return "".join([random.choice(charset) for _ in range(l)])

if __name__ == "__main__":
    random.seed(42)
    n = 10 ** 5
    m = set()

    for i in range(2*n-1):
        while True:
            x = flag(random_string(10))
            if x not in m:
                m.add(x)
                break

    m = list(m)
    A = m[:n-1]
    B = m[n-1:2*n-1]
    A.append(m[-1])
    B.append(m[-1])
    random.shuffle(A)
    random.shuffle(B)


    with open("script.py", "w") as f:
        f.write('"' * 3)
        f.write("\nA : A list with 100 thousand unique strings")
        f.write("\nB : A list with 100 thousand unique strings\n")
        f.write('"' * 3)
        f.write(f"""\nA = {A}""")
        f.write(f"""\nB = {B}\n""")
        