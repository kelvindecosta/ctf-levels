import random

if __name__ == "__main__":
    random.seed(42)
    DATA = set()
    for i in range(10 ** 3):
        while True:
            x = random.randint(1, 10 ** 6)
            if x not in DATA:
                DATA.add(x)
                break

    with open("script.py", "w") as f:
        f.write('"' * 3)
        f.write("\nDATA : A set of 1 thousand randomly generated numbers between 1 and 1 million\n")
        f.write('"' * 3)
        f.write(f"\nDATA = {DATA}\n")