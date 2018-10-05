from urllib.request import urlopen
import sys

def words_per_file(flo):
	return [len(line.split()) for line in flo.readlines()]

def showcount(link):
	with urlopen(link) as webfile:
		wpl = words_per_file(webfile)
	
	print(wpl)

def main(link):
	showcount(link)

if __name__ == '__main__':
	main(sys.argv[1])

