from factordb.factordb import FactorDB
import gmpy2
from Crypto.Util.number import *


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


def rsa_decrypt_nec(n, e, c):
    if e <= 3:
        step = 2
        (t1, t2) = gmpy2.iroot(c, e)
        while not t2:
            (t1, t2) = gmpy2.iroot(c + step * n, e)
            step += 1
        return t1
    else:
        d = crack_d(n, e)
        if d != -1:
            return rsa_decrypt_ndc(n, d, c)
        else:
            return -1


def rsa_decrypt_ndc(n, d, c):
    return pow(c, d, n)


def crack_rsa(n, d=0, e=0, c=0, mode=0):
    if mode == 0:
        return rsa_decrypt_ndc(n, d, c)
    elif mode == 1:
        return rsa_decrypt_nec(n, e, c)


def main():
    res = crack_rsa(
        n=82905415164584389498448026225415348174116889583631879848801181149026319038674433017502044002549515598507479948874775953835212967198538225241428587373756775740055748735130854340971352961320030869329470225485298576771293717521094156379711969189220894688314434350844834550493516522022887482934023393062055248939,
        e=3,
        c=1235510871330310226418475368687292699345971692547143305272739246584681306551612197261843363110934247264155805712224284359950318209523214607727920666576650829438419066769737275066742744939310467207427865797663652787759689887376716363284875754160160311515163574335764507693157,
        mode=1,
    )
    if res != -1:
        print(long_to_bytes(res).decode())
    else:
        print("fail QQ")


if __name__ == "__main__":
    main()
