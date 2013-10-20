"""
One problem we face when implementing this program is that the name of the
substance can contain one or two words, and maybe more words in a more
comprehensive table.

The purpose of this exercise is to use string operations to shorten the code
and make it more general. Implement the following two methods in separate
functions in the same program, and control that they give the same result. 

    1. Let substance consist of all the words but the last, using the join
       method in string objects to combine the words.
    2. Observe that all the densities start in the same column file and use
       substrings to divide line into two parts. (Hint: Remember to strip
       the first part such that, e.g., the density of ice is obtained as
       densities['ice'] and not densities['ice       '].)
"""

# Start new methods:
def read_substance(words):
    substance = ''
    for word in words[:-1]:
        substance = substance + word + ' '
    return substance.rstrip() # Removes last space

def read_density(line):
    return float(line[13:])
# End new methods


def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()

        """
        # Old code
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]
        """

        # Start new code
        density = read_density(line)
        substance = read_substance(words)
        # End new code


        densities[substance] = density
    infile.close()
    return densities

densities = read_densities('src/files/densities.dat')
from scitools.pprint2 import pprint
pprint(densities)

"""
$ python 6.10_density_improved.py 
{'Earth core': 3,
 'Earth mean': 0.52,
 'Moon': 0.3,
 'Sun core': 60,
 'Sun mean': 0.4,
 'air': 0.0012,
 'gasoline': 0.67,
 'gold': 8.9,
 'granite': 0.7,
 'human body': 0.03,
 'ice': 0.9,
 'iron': 0.8,
 'limestone': 0.6,
 'mercury': 3.6,
 'platinium': 1.4,
 'proton': 8e+13,
 'pure water': 0,
 'seawater': 0.025,
 'silver': 0.5}
"""
