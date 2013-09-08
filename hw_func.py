# 3.12 
# yay, functions!
def hw1():
    return 'Hello World!'

#fucntions must be called
output = hw1()
print output

def hw2():
    print 'Hello World!'
    return None # will default to this if function has no return line. None is case sensitive!

hw2()

def hw3(string1, string2):
    print '%s, %s' % (string1, string2)
    
    # print string1 + ',' + string2

hw3('Hello' ,'World!')

