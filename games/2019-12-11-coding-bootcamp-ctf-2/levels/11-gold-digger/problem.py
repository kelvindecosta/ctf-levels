import random


if __name__ == "__main__":
	random.seed(42)
	with open("input.txt", "w") as f:
		T = 1
		D = 100
		V = 100
		f.write(str(T) + "\n")

		for _ in range(T):
			m = D
			n = D
			f.write(f"{m} {n}" + "\n")

			for _ in range(m):
				l = [random.randrange(V + 1) for _ in range(n)]
				f.write(" ".join(map(str, l)) + "\n")
