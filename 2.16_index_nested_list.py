# Exercise 2.19. Index a nested lists.
# We define the following nested list:
# q = [['a','b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
# Index this list to extract 1) the letter a; 2) the list ['d', 'e', 'f'];
# 3) the last element h; 4) the d element. Explain why q[-1][-2] has the
# value g. Name of program file: index_nested_list.py


# Yo dawg, I know you like lists so I put 3 lists in your list
q = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h']
    ]

#1
print q[0][0]

#2
print q[1]

#3
print q[-1][-1]

#4
print q[-1][-2] #last list, last but one element of that list
