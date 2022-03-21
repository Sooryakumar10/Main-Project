from collections import namedtuple
from random import *
Point = namedtuple("Point", "x y")

original='HI THIS IS COA'
eO = 'ORIGIN'
ep =71
ea = 1
eb = 3
ena=randint(1,ep-1)
enb=randint(1,ep-1)
k=randint(1,ep-1)
eg='35,10'
epa=epb=ekpb=nbkg=''

bina=''
pt=[]

radix = []
for i in range(65, 91):
    radix.append(chr(i))
for i in range(97, 123):
    radix.append(chr(i))
for i in range(10):
    radix.append(str(i))
radix.append('+')
radix.append(',')

points = []
lhs = rhs = 0
for i in range(ep):
    for j in range(ep):
        lhs = (j * j) % ep
        rhs = ((i * i * i) + (ea*i) + eb) % ep
        if lhs == rhs:
            points.append(str(i) + ',' + str(j))
points.append(eO)

def valid(P):
    if P == eO:
        return True
    else:
        return (
            (P.y**2 - (P.x**3 + ea*P.x + eb)) % ep == 0 and
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

nat=ena
xp=xq=int(eg.split(',')[0])
yp=yq=int(eg.split(',')[1])
P=Point(xp,yp)
Q=Point(xq,yq)
if ena==1:
    epa=eg
else:
    while nat!=1:
        r=ec_add(P,Q)
        if r==eO:
            P=r
        else:
            xp=r.x
            yp=r.y
            P=Point(xp,yp)
        nat=nat-1
    if r==eO:
        epa=r
    else:
        epa=str(xp)+','+str(yp)

nat=enb
xp=xq=int(eg.split(',')[0])
yp=yq=int(eg.split(',')[1])
P=Point(xp,yp)
Q=Point(xq,yq)
if enb==1:
    epb=eg
else:
    while nat != 1:
        r = ec_add(P,Q)
        if r == eO:
            P = r
        else:
            xp = r.x
            yp = r.y
            P = Point(xp, yp)
        nat=nat-1
    if r == eO:
        epb = r
    else:
        epb = str(xp) + ',' + str(yp)

nat = k
if k==1:
    ekpb=epb
else:
    if epb==eO:
        P=Q=eO
        while nat != 1:
            r = ec_add(P, Q)
            if r == eO:
                P = r
            else:
                xp = r.x
                yp = r.y
                P = Point(xp, yp)
            nat=nat-1
        if r == eO:
            ekpb = r
        else:
            ekpb = str(xp) + ',' + str(yp)
    else:
        xp = xq = int(epb.split(',')[0])
        yp = yq = int(epb.split(',')[1])
        P=Point(xp,yp)
        Q=Point(xq,yq)
        while nat != 1:
            r = ec_add(P, Q)
            if r == eO:
                P = r
            else:
                xp = r.x
                yp = r.y
                P = Point(xp, yp)
            nat=nat-1
        if r == eO:
            ekpb = r
        else:
            ekpb = str(xp) + ',' + str(yp)
temp=original

for i in temp:
    bina = bina + format(ord(i), '08b')
if len(bina) % 6!= 0:
    for i in range((6 - (len(bina) % 6))):
        bina = bina + str(0)
bina.replace('0b', '')
i = 0
while (i != len(bina)):
    t = bina[i:i + 6]
    t = '0b' + t
    t = int(t, 2)
    pt.append(points[t])
    i = i + 6
for ok in pt:
    if ok==eO:
        P=eO
    else:
        t = ok.split(',')
        P=Point(int(t[0]),int(t[1]))
    if ekpb==eO:
        Q=eO
    else:
        Q=Point(int(ekpb.split(',')[0]),int(ekpb.split(',')[1]))
    r=ec_add(P,Q)
    if r==eO:
        pt[pt.index(ok)] = radix[points.index(eO)]
    else:
        xp = r.x
        yp = r.y
        pt[pt.index(ok)] =radix[points.index(str(xp) + ',' + str(yp))]

ct=''.join(pt)
ct1=ct

print('Encrypted Text=',ct1)

nat = k*enb
if epb==eO:
    P=Q=eO
else:
    xp = xq = int(eg.split(',')[0])
    yp = yq = ep-int(eg.split(',')[1])
    P = Point(xp, yp)
    Q = Point(xq, yq)
if nat == 1:
    nbkg = eg
else:
    while nat != 1:
        r = ec_add(P, Q)
        if r == eO:
            P = r
        else:
            xp = r.x
            yp = r.y
            P = Point(xp, yp)
        nat=nat-1
    if r == eO:
        nbkg = r
    else:
        nbkg = str(xp) + ',' + str(yp)


bina = ''
ct=[]
for i in ct1:
    ct.append(points[radix.index(i)])
for ok in ct:
    if ok == eO:
        P = eO
    else:
        t = ok.split(',')
        P = Point(int(t[0]), int(t[1]))
    if nbkg == eO:
        Q = eO
    else:
        Q = Point(int(nbkg.split(',')[0]), int(nbkg.split(',')[1]))
    r = ec_add(P, Q)
    if r == eO:
        ct[ct.index(ok)] = points.index(eO)
    else:
        xp = r.x
        yp = r.y
        ct[ct.index(ok)] = points.index(str(xp) + ',' + str(yp))
for i in ct:
    bina = bina + format(i, '06b')
if len(bina) % 8 != 0:
    for i in range((8 - (len(bina) % 8))):
        bina = bina + str(0)
bina.replace('0b', '')
i = 0
ct = []
while (i != len(bina)):
    t = bina[i:i + 8]
    t = '0b' + t
    t = int(t, 2)
    ct.append(chr(t))
    i = i + 8

pt1=''.join(ct)
pt1=pt1.rstrip('\x00')
print('Decrypted Text=',pt1)

