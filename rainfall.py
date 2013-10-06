infile = open('examples/files/rainfall.dat','r')
infile.readline() # skip line 1
numbers = []

for line in infile:
    words = line.split() # splits on space as deault
    number = float(words[1])
    numbers.append(number)

infile.close
print numbers
