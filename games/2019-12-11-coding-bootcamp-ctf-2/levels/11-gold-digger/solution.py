def move(i, j, gold, grid):
	m, n = len(grid), len(grid[0])

	if i == m - 1:		# reached the bottom-most row in the grid
		while j < n:	# only option is to go right
			gold += grid[i][j]
			j += 1
	elif j == n - 1:	# reached the right-most column in the grid
		while i < m:	# only option is to go down
			gold += grid[i][j]
			i += 1
	else:				# go both paths (down and right), take path with maximum gold
		gold = grid[i][j] + max(move(i + 1, j, gold, grid), move(i, j + 1, gold, grid))

	return gold

def dynamic_programming(grid):
	m, n = len(grid), len(grid[0])
	dp = [[0] * n for _ in range(m)]

	# Base cases
	dp[0][0] = grid[0][0]	# initialize starting position

	for i in range(1, n):	# initialize first row
		dp[0][i] = grid[0][i] + dp[0][i - 1]

	for i in range(1, m):	# initialize first column
		dp[i][0] = grid[i][0] + dp[i - 1][0]

	# Dynamic Programming
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

	return dp[m - 1][n - 1]


def nextline(lines):
	return lines.pop(0)


if __name__ == '__main__':
	with open("input.txt", "r") as f:
		lines = f.read().strip().split("\n")
		T = int(nextline(lines))

		for _ in range(T):
			m, n = map(int, nextline(lines).split())
			grid = [list(map(int, nextline(lines).split())) for _ in range(m)]
			# print(move(0, 0, 0, grid))
			print("CTF{" + str(dynamic_programming(grid)) + "}")
