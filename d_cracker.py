from factordb.factordb import FactorDB
import gmpy2

def factorize_with_factorDB(n):
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()
    if len(factors) == 1:
        return [-1]
    return factors


def factorize_with_Pollard(n, B=2000):
    if gmpy2.is_prime(n):
        return [n]
    a = 2
    i = 2
    while i < B:
        a = pow(a, i, n)
        d = gmpy2.gcd(a - 1, n)
        if d != 1:
            return [d] + factorize_with_Pollard(n // d)
        else:
            i += 1
    return [-1]


def factorize_with_fermat(n):
    a = gmpy2.iroot(n, 2)[0]
    while True:
        b1 = a * a - n
        (b, t) = gmpy2.iroot(b1, 2)
        if t:
            return [a + b, a - b]
        a += 1


def crack_d(n, e):
    flist = [factorize_with_factorDB, factorize_with_Pollard, factorize_with_fermat]
    factors = [-1]
    for f in flist:
        factors = f(n)
        if factors != [-1]:
            break
    else:
        return -1
    phi_n = 1
    for i in factors:
        phi_n *= i - 1
    d = gmpy2.invert(e, phi_n)
    return d
