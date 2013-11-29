print "Ex. 8.5"
import sys, random

def roll_dice():
    return random.randint(1, 6)

def do_experiment(case):
    if case == 1:
        return roll_dice() == 6
    elif case == 2:
        for i in range(4):
            if roll_dice() != 6:
                return False
        return True

    elif case == 3:
        three_consecutive = False
        while (not three_consecutive):
            first = roll_dice()
            second = roll_dice()
            third = roll_dice()
            print "%d %d %d" % (first, second, third)
            three_consecutive = (first == 6 and second == 6 and third == 6)

        return roll_dice() == 6
    
    else:
        raise ValueError("Unknown experiment case")

case = int(sys.argv[1])
num_experiments = int(sys.argv[2])
num_success = 0

for i in range(num_experiments):
    if do_experiment(case):
        num_success += 1

print num_success/float(num_experiments)
