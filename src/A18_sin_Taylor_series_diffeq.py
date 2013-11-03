"""
Man har en funksjon som er vanskelig aa ha med aa gjorere, f.ex. sin(x). Vi kan da bruke Taylor polynomer for aa finne et uttrykk for f(x) i et arbitraert punkt.

Det fordrer at man vet den deriverte for et punkt a.
"""

def sine_Taylor(x, N):
    x = float(x)
    a_prev = x
    s_prev = 0.0

    for j in range(1, N):
        a_current = -x**2/((2*j+1)*2*j) * a_prev
        s_current = s_prev - a_prev

        a_prev = a_current
        s_prev = s_current

    return s_prev, a_prev

print sine_Taylor(1.0, 10)
