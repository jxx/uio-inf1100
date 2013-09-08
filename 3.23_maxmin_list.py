# Find the max and in in a list
# max() and min() exist in the std library, but here we create them ourselves

a = [3,7,9,1,3,5,-100,100]

def max(a):
    a_max = a[0]
    for element in a[1:]:
        if element > a_max:
            a_max = element
    return a_max

print max(mylist)

