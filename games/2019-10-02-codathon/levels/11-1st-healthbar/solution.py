if __name__ == "__main__":
    with open("p1.txt", "rb") as f:
        p1 = f.read()

    with open("p2.txt", "rb") as f:
        p2 = f.read()
    
    print(bytes(a ^ b for (a, b) in zip(p1, p2)).decode("utf-8"))