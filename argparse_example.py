import argparse

#Sets up the program to read command line arguments

parser = argparse.ArgumentParser(description = 'Compare two result sets')

parser.add_argument('file1', type=str, help='Filename of first result set')
parser.add_argument('file2', type=str, help='Filename of second result set')

parser.add_argument('--verbose', action='store_true', help='Be a little more verbose') #Adds a new argument option to the program, --verbose, which does not take any values

args = parser.parse_args()

print args.file1
print args.file2

if args.verbose:
    print "Verbose"
else:
    print "Not verbose"
