from collections import namedtuple
from random import *
Point = namedtuple("Point", "x y")

def valid(P):
    if P == eO:
        return True
    else:
        return (
            (P.y*2 - (P.x*3 + ea*P.x + eb)) % ep == 0 and
            0 <= P.x < ep and 0 <= P.y < ep)
def inv_mod_p(x):
    if x % ep == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, ep-2, ep)

def ec_inv(P):
    if P == eO:
        return P
    return Point(P.x, (-P.y)%ep)

def ec_add(P, Q):
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid inputs")

    if P == eO:
        result = Q
    elif Q == eO:
        result = P
    elif Q == ec_inv(P):
        result = eO
    else:
        if P == Q:
            dydx = (3 * P.x**2 + ea) * inv_mod_p(2 * P.y)
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
        x = (dydx**2 - P.x - Q.x) % ep
        y = (dydx * (P.x - x) - P.y) % ep
        result = Point(x, y)

    assert valid(result)
    return result