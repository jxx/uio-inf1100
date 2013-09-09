eps = 1.0

while 1.0 != 1.0 + eps:
    print '...............',eps
    eps /= 2.0
print 'final eps:', eps
"""
1.0 is actually 1.0 +- a small value, around 1E-16

"""
$ python 2.23_machine_zero.py 
............... 1.0
............... 0.5
............... 0.25
............... 0.125
............... 0.0625
............... 0.03125
............... 0.015625
............... 0.0078125
............... 0.00390625
............... 0.001953125
............... 0.0009765625
............... 0.00048828125
............... 0.000244140625
............... 0.0001220703125
............... 6.103515625e-05
............... 3.0517578125e-05
............... 1.52587890625e-05
............... 7.62939453125e-06
............... 3.81469726562e-06
............... 1.90734863281e-06
............... 9.53674316406e-07
............... 4.76837158203e-07
............... 2.38418579102e-07
............... 1.19209289551e-07
............... 5.96046447754e-08
............... 2.98023223877e-08
............... 1.49011611938e-08
............... 7.45058059692e-09
............... 3.72529029846e-09
............... 1.86264514923e-09
............... 9.31322574615e-10
............... 4.65661287308e-10
............... 2.32830643654e-10
............... 1.16415321827e-10
............... 5.82076609135e-11
............... 2.91038304567e-11
............... 1.45519152284e-11
............... 7.27595761418e-12
............... 3.63797880709e-12
............... 1.81898940355e-12
............... 9.09494701773e-13
............... 4.54747350886e-13
............... 2.27373675443e-13
............... 1.13686837722e-13
............... 5.68434188608e-14
............... 2.84217094304e-14
............... 1.42108547152e-14
............... 7.1054273576e-15
............... 3.5527136788e-15
............... 1.7763568394e-15
............... 8.881784197e-16
............... 4.4408920985e-16
............... 2.22044604925e-16
final eps: 1.11022302463e-16
"""
