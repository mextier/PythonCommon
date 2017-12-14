import os

fn = "filetest.txt"
with open(fn,'w') as f:
	for i in range(1,11):
		f.write('Number {}\n'.format(i))
	#f.close()

f = open(fn,"r")
alllines=[line.strip() for line in f]
f.close()

print(alllines)
os.remove(fn)




