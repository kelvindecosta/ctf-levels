def count(x):
	s = (x >= 10)
	while (x):
		mod = x % 10
		if x < 10 or mod == 0:
			s += 9
		else:
			s += 9 - mod
		x //= 10
	return s


if __name__ == "__main__":
	print("CTF{" + str(count(12345678987654321)) + "}")
