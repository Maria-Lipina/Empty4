#lcm - lowest common multiple, наименьшее общее кратное
#gcd - greatest common divisor, наибольший общий делитель

from math import gcd, lcm
import primes

def LCM (n: int, m: int):
    """Вычисляет наименьшее общее кратное для двух целых чисел n, m"""

    a = primes.factors(n)
    b = primes.factors(m)
    c = a | b
    d = list(a.keys() & b.keys())
    for i in d:
        if a[i] > b[i]: c[i] = a[i]

    e = list(c)
    lcm = 1
    for j in e:
        lcm = lcm * (j ** c[j])
    return lcm

def LCM2 (n: int, m: int):
    """Вычисляет наименьшее общее кратное для двух целых чисел n, m"""

    return abs((n * m)) // gcd(n , m)


def LCM3 (n: int, m: int):
    """Вычисляет наименьшее общее кратное для двух целых чисел n, m"""

    return lcm(n, m)