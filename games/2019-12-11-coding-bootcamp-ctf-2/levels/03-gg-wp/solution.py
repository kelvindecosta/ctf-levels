import re


if __name__ == "__main__":
    r = re.compile(r"(\w+) defeated (\w+)")

    winners = set()
    losers = set()

    with open("input.txt", "r") as f:
        for line in  f.read().strip().split("\n"):
            g = r.match(line).groups()
            winners.add(g[0])
            losers.add(g[1])

    print("CTF{" + (winners-losers).pop() + "}")
