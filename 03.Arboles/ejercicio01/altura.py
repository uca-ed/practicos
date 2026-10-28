import math

def calcular_altura(r: int, n: int) -> int:

    if n <= 0:
        return 0

    if r == 1:
        return n

    # h = log_r(n * (r - 1) + 1)
    val = n * (r - 1) + 1
    h = math.log(val, r)

    return round(h)