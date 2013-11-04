# IPython log file

cls
get_ipython().system(u'clear ()')
import random
import numpy as np
get_ipython().magic(u'timeit')
get_ipython().magic(u'logstart Oct30.py')
import random
import numpy as np
get_ipython().magic(u'timeit')
n = 1000000
get_ipython().magic(u'timeit r = [random.random() for i in range(n)]')
get_ipython().magic(u'timeit r = [np.random() for i in range(n)]')
get_ipython().magic(u'timeit r = [np.random.random() for i in range(n)]')
get_ipython().magic(u'timeit r = np.random.random(nize=n)')
get_ipython().magic(u'timeit r = np.random.random(size=n)')
quit()
