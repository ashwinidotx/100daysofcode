import sys

def words_per_file(flo):
	return [len(line.split()) for line in flo.readlines()]

def showcount(filename):
	with open(filename, mode = 'rt', encoding = 'utf-8') as file:
		wpl = words_per_file(file)
	
	print(wpl)

def main(link):
	showcount(link)

if __name__ == '__main__':
	main(sys.argv[1])

