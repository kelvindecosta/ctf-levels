import random
import string


def name():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(8, 10)))


if __name__ == "__main__":
    random.seed(42)

    # Create a set of usernames
    names = set()
    for _ in range(100):
        while True:
            n = name()
            if n not in names:
                names.add(n)
                break

    # Assign one username as the winner
    best = random.choice(sorted(names))

    # Generate games
    games = set()
    for n in names:
        for _ in range(7):
            while True:
                p1 = n
                p2 = random.choice(sorted(names - set([p1, best])))
                if (p1, p2) not in games:
                    games.add((p1, p2))
                    break

        for _ in range(3):
            while True:
                if n != best:
                    p1 = random.choice(list(names - set([n])))
                    p2 = n
                else:
                    p1 = random.choice(list(names - set([best])))
                    p2 = random.choice(list(names - set([p1, best])))

                if (p1, p2) not in games:
                    games.add((p1, p2))
                    break


    with open("input.txt", "w") as f:
        for g in games:
            f.write(f"{g[0]} defeated {g[1]}")
            f.write("\n")
