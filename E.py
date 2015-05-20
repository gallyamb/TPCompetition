from math import sqrt, sin, cos


def generate_func():
	code = input().replace('^', '**')

	def f(x):
		return eval(code)

	return f

def get_numeric_integral(start, finish, f):
	result = 0
	for i in range(start * 10, finish * 10, 1):
		result += abs(f(i / 10 + 0.05) * (0.1))
	return result

start, finish = tuple(map(int, input().split()))
func = generate_func()
print(get_numeric_integral(start, finish, func))
