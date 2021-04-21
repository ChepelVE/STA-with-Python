import math
from typing import List


def cont_fraction(fraction: str) -> str:
    ip, fp = map(int, fraction.split("/"))
    cf = []

    def cont_fraction_recursive(ip: int, fp: int) -> List:
        try:
            a = math.floor(ip / fp)
        except ZeroDivisionError:
            print("Invalid fraction!")
            return -1
        cf.append(str(a))
        if ip % fp != 0:
            ip -= a * fp
            return cont_fraction_recursive(fp, ip)

    cont_fraction_recursive(ip, fp)
    result = " ".join(cf)
    print("Continued fraction for {} is: {}".format(fraction, result))
    return result

