import os, sys, random, string

forselect = string.letters + string.digits
path = os.path.join(sys.path[0], "codelist.txt")
txt = open(path, "w")

def generate_code(count, length):
	for x in range(count):
		for y in range(length):
			codes = random.choice(forselect)
#			print "codes is : %s" %codes
			txt.write(''.join(codes))
		txt.write("\n")
	txt.close()
	
	
if __name__ == "__main__":
	m = int(raw_input("please type the count: "))
	n = int(raw_input("please type the length: "))
	generate_code(m, n)