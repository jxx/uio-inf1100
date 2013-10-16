def poly_list_eval(polynom, x):
    if not isinstance(polynom, list):
        raise TypeError ("Argument must be a list")
    return sum([polynom[i] * x**i for i in range(len(polynom))])

#    Longform:
#    sum - 0.0
#    for i in polynom:
#        sum += polynom[i] * x**i

def poly_dict_eval(polynom, x):
    return sum([polynom[exp] * x ** i for exp in polynom])

#    Longform:
#    s = 0.0
#    for exp in polynom: # no length, dict returns the key themselves
#        s += polynom[exp] * x**exp

    return s

p_list =  [0.0]*101
p_list[0] = -.5
p_list[100] = [2.0]


poly_list_eval(p_list, 1.05)


p_dict = {0 : -.5, 100: 2.0}

poly_dict_eval(p_dict, 1.05)


print poly_list_eval
print poly_dict_eval
