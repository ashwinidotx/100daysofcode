import sys
"""File opening using 'with' for no memory leaks
"""
def series(filename):
	with open(filename, mode='rt', encoding='utf-8') as f:
		return [line.strip() for line in f]
# 'with' removes the need for explicit close()
def main(filename):
	r_series = series(filename)
	print(r_series)

if __name__ == '__main__':
	main(sys.argv[1])