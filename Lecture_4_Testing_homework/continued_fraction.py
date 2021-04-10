import math
from typing import List


def cont_fraction(fraction: str) -> str:
    ip = int(fraction.split("/")[0])
    fp = int(fraction.split("/")[1])
    cf = []

    def cont_fraction_recursive(ip: int, fp: int) -> List:
        a = math.floor(ip / fp)
        cf.append(str(a))
        if ip % fp != 0:
            ip -= a * fp
            return cont_fraction_recursive(fp, ip)

    cont_fraction_recursive(ip, fp)
    result = " ".join(cf)
    print("Continued fraction for {} is: {}".format(fraction, result))
    return result

