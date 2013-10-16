"""Make a nested dictionary from a file and print it"""

def parse_file(filename):
    f = open(filename, 'r')


    humans = {}
 
    for line in f:
        if not line.startswith("H."):
            continue

        name = line[:21].strip()
        name = name.replace("H.", "Homo")
        humans[name] = { "when" : line[21:37].strip(),
                         "height" : line[37:51].strip(),
                         "weight" : line[51:63].strip(),
                         "brain vol" : line[63:].strip() }
    return humans


def print_table(humans):
    print "Species              Lived when      Adult        Adult       Brain vol"
    print "                     (mill. yrs)     height (m)   mass (kg)   (cm**3) "
    print "-" * 72
    
    for species in humans:
        print species.ljust(20, " "), 
        humans[species]["when"].ljust(16, " "),
        humans[species]["height"].ljust(13, " "),
        humans[species]["weight"].ljust(12, " "),
        humans[species]["brain vol"]


text = parse_file('human_evolution.txt')
print_table(text)
