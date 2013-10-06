"""
Text in Python is represented as strings
Programming with strings is therefore the key to interpret text
in files and construct new text
First we show some common string operations and then we
apply them to real examples
Our sample string used for illustration is
>>> s = ’Berlin: 18.4 C at 4 pm’
Strings behave much like lists/tuples - they are a sequence of
characters:
>>> s[0]
'B'
>>> s[1]
'e'

Substrings are just as slices of lists and arrays:
>>> s
’Berlin: 18.4 C at 4 pm’
>>> s[8:]
# from index 8 to the end of the string
’18.4 C at 4 pm’
>>> s[8:12]
# index 8, 9, 10 and 11 (not 12!)
’18.4’
>>> s[8:-1]
’18.4 C at 4 p’
>>> s[8:-8]
’18.4 C’
Find start of substring:
>>> s.find(’Berlin’) # where does ’Berlin’ start?
0                    
>>> s.find(’pm’)     # at index 0
20                   
>>> s.find(’Oslo’)   # not found
-1 #could have returned a none, but programing convention returns a -1 in these cases.

>>> ’Berlin’ in s:
True
>>> ’Oslo’ in s:
False
>>> if ’C’ in s:
...
print ’C found’
... else:
...
print ’no C’
...
C found


Example: replacing the text before the first colon by ’Bonn’
\>>> s
’Berlin: 18.4 C at 4 pm’
>>> s.replace(s[:s.find(’:’)], ’Bonn’) # from start of string to index where it fins
’Bonn: 18.4 C at 4 pm’


Try to understand this one:
# split fist once based on : then on space, then convert.
>>> s.split(’:’)[1].split()[0] 
’18.4’
>>> deg = float(_) # convert last result to float
>>> deg
18.4
"""
