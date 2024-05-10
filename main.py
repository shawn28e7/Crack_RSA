from Crypto.Util.number import *
import gmpy2
from d_cracker import crack_d


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
        if d is None:
            return None
        else:
            return rsa_decrypt_ndc(n, d, c)


def rsa_decrypt_ndc(n, d, c):
    return pow(c, d, n)


def crack_rsa(n, d=0, e=0, c=0, mode=0):
    if mode == 0:
        return rsa_decrypt_ndc(n, d, c)
    elif mode == 1:
        return rsa_decrypt_nec(n, e, c)
    else:
        raise ValueError("mode is neither 0 nor 1")


def main():
    res = crack_rsa(
        n=82905415164584389498448026225415348174116889583631879848801181149026319038674433017502044002549515598507479948874775953835212967198538225241428587373756775740055748735130854340971352961320030869329470225485298576771293717521094156379711969189220894688314434350844834550493516522022887482934023393062055248939,
        e=3,
        c=1235510871330310226418475368687292699345971692547143305272739246584681306551612197261843363110934247264155805712224284359950318209523214607727920666576650829438419066769737275066742744939310467207427865797663652787759689887376716363284875754160160311515163574335764507693157,
        mode=1,
    )
    if res is None:
        print(long_to_bytes(res).decode())
    else:
        print("fail QQ")


if __name__ == "__main__":
    main()
