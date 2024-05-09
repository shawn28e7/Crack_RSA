from factordb.factordb import FactorDB
import gmpy2
from Crypto.Util.number import *

def crack_d_factorDB(n, e):
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()
    phi_n = 1
    for i in factors:
        phi_n *= (i - 1)
    d = inverse(e, phi_n)
    return d

def rsa_decrypt_nec(n, e, c):
    if e <= 5:
        step = 2
        (t1, t2) = gmpy2.iroot(c, e)
        while not t2:
            (t1, t2) = gmpy2.iroot(c + step * n, e)
            step += 1
        return t1
    else:
        d = crack_d_factorDB(n, e)
        return rsa_decrypt_ndc(n, d, c)


def rsa_decrypt_ndc(n, d, c):
    return pow(c, d, n)

def crack_rsa(n, d = 0, e = 0, c = 0, mode = 0):
    if mode == 0:
        return rsa_decrypt_ndc(n, d, c)
    elif mode == 1:
        return rsa_decrypt_nec(n, e, c)

def main():
    res = crack_rsa(n = 641038552669922004650640356715638051098436533497923620822471,
e = 65537,
c = 537756663490573782815200170116248828935623440674192611059116, mode = 1)
    print(long_to_bytes(res).decode())

if __name__ == "__main__":
    main()