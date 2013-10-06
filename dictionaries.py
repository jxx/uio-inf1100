# Suppose we need to store the temperatures in Oslo, London and Paris

#list method, not very useful:
temps = [13, 15.4, 17.5]
# temps[0]: Oslo
# temps[1]: London
# temps[2]: Paris


# Dictioinaries are unsorted hashmaps
temp_dic = {'Oslo' : 13.0, 'London': 15.4, 'Paris' : 17.5 }

print temp_dic['Paris'] # Uses Hashmap, no performance diff for 1 bln long dict.

for city in temp_dic:
    print 'the temp in %s is %g' % \
        (city, temp_dic[city])

#keys and values can be recehd as lists:
temps.keys()

#A polynomial can be represented by a dict with poert as key and coefficiant as value

p = {0: -1, 2: 2, 7: 3}

def poly1(data, x):
    sum = 0.0
    for power in data:
        sum += data[power]*x**power
    return sum

# A list can also represent a poly, and are better to store in than in lists, as lists require housekeeping for negative powers, dictionaries can have floats as indices etc.

#Begreper: sparse = lagrer ikke nuller, dense = lagrer alle nuller


# Loading data:

infile = open('examples/data/deg2.dat', 'r')
temps = {}  # start with empty dic

# Dictionaries allow dictionaries of dictionaries, for more dimensions. This might get tricky with all the nested indexes.

