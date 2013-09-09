"""
Heaviside function. Implement 
H(x) = 0 for x < 0
H(x) = 1 for x >= 0 
"""

def heaviside(x):
    if x < 0:
        return 0
    else:
        return 1

for x in [-0.5, 0, 10]:
    print heaviside(x)

"""
$ python 3.24_Heaviside.py 
0
1
1
"""
