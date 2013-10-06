infile = open('examples/files/data1.txt', 'r')

#for line in infile: #reads one and one line
#    print line

lines = infile.readlines() #Reads entire file at once

mean = 0
for number in lines: #number here is a STRING
    mean = mean + float(number)
mean = mean / len(lines)
print mean

#for line in inlines:
    #process lines

counter = 0

for line in infile:
    sum += foat(line)
    counter = counter + 1


print mean

numbers = [float(line) for line in infile.readlines()]

mean = sum(numbers)/len(numbers)
print mean


infile.close()
