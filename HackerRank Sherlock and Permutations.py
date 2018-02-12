import math

def alg(n, m):
	if m == 0:
		return 0

	if m == 1:
		return 1

	else:
		x = factorial((m - 1) + n)
		y = factorial(n)
		z = factorial(m - 1)

		return ((x / (y * z)) % (pow(10, 9) + 7))

def factorial(n):
	i = 1
	for x in range (1, n + 1):
		i = i * x

	return i

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print alg(n, m)