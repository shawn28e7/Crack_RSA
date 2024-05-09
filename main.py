from factordb.factordb import FactorDB
import BigNumber
import gmpy2
from Crypto.Util.number import *

def rsa_decrypt(n, e, c):
    if e <= 5:
        step = 2
        (t1, t2) = gmpy2.iroot(c, e)
        while not t2:
            (t1, t2) = gmpy2.iroot(c + step * n, e)
            step += 1
        return t1


def rsa_decrypt(n, d, c):
    return pow(c, d, n)

def main():
    rsa_decrypt()


if __name__ == "__main__":
    main()