import hashlib
from collections import namedtuple
from random import *
import numpy
import points as points

Point = namedtuple("Point", "x y")
import pymongo

# To Establish Connection with Cloud
file_id = int(input("Enter the id of file to Decrypt : "))
client = pymongo.MongoClient("mongodb+srv://soorya:soorya@cluster0.hl7ws.mongodb.net/Main?retryWrites=true&w=majority")
db = client["Main"]
collections = db["Main"]
cloud_data = collections.find_one({"_id": file_id})
print(cloud_data)

# Getting the encrypted information from cloud
encrypted_output = cloud_data.get('Encrypted information')
print(encrypted_output)

# Getting the key of Dehex From the Cloud
encrypt_key_from_cloud = cloud_data.get('Key_Dehex')
print(encrypt_key_from_cloud)

# Getting the key_id.txt from Local Directory
message1 = ""
input_key_file = input("Enter your file name : ")
inputFile = open(input_key_file, 'r')
for line in inputFile:
     message1 = message1 + line

# Applying SHA to the Key_id.txt
result = hashlib.sha256(input_key_file.encode())
print("The hexadecimal equivalent of SHA256 is : ")
sha_decryption = result.hexdigest()
print(sha_decryption)

def ECC_Decryption():
    original = encrypted_output
    eO = 'ORIGIN'
    ep = 71
    ea = 1
    eb = 3
    ena = randint(1, ep - 1)
    enb = randint(1, ep - 1)
    k = randint(1, ep - 1)
    eg = '35,10'
    epa = epb = ekpb = nbkg = ''

    bina = ''
    pt = []

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
            rhs = ((i * i * i) + (ea * i) + eb) % ep
            if lhs == rhs:
                points.append(str(i) + ',' + str(j))
    points.append(eO)


    def valid(P):
        if P == eO:
            return True
        else:
            return (
                    (P.y ** 2 - (P.x ** 3 + ea * P.x + eb)) % ep == 0 and
                    0 <= P.x < ep and 0 <= P.y < ep)


    def inv_mod_p(x):
        if x % ep == 0:
            raise ZeroDivisionError("Impossible inverse")
        return pow(x, ep - 2, ep)


    def ec_inv(P):
        if P == eO:
            return P
        return Point(P.x, (-P.y) % ep)


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
                dydx = (3 * P.x ** 2 + ea) * inv_mod_p(2 * P.y)
            else:
                dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
            x = (dydx ** 2 - P.x - Q.x) % ep
            y = (dydx * (P.x - x) - P.y) % ep
            result = Point(x, y)

        assert valid(result)
        return result

    nat = k * enb
    if epb == eO:
        P = Q = eO
    else:
        xp = xq = int(eg.split(',')[0])
        yp = yq = ep - int(eg.split(',')[1])
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
            nat = nat - 1
        if r == eO:
            nbkg = r
        else:
            nbkg = str(xp) + ',' + str(yp)

    bina = ''
    ct = []
    for i in original:
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

    pt1 = ''.join(ct)
    pt1 = pt1.rstrip('\x00')
    print('Decrypted Text=', pt1)
    return pt1
    #-------------------------------------------------------------------------------
    # ct1 = encrypted_output
    # eO = 'ORIGIN'
    # ep = 71
    # ea = 1
    # eb = 3
    # ena = 47
    # enb = 8
    # k = 30
    # eg = '35,10'
    # epa = epb = ekpb = nbkg = ''
    #
    # radix = []
    # for i in range(65, 91):
    #     radix.append(chr(i))
    # for i in range(97, 123):
    #     radix.append(chr(i))
    # for i in range(10):
    #     radix.append(str(i))
    # radix.append('+')
    # radix.append(',')
    #
    # points = []
    # lhs = rhs = 0
    # for i in range(ep):
    #     for j in range(ep):
    #         lhs = (j * j) % ep
    #         rhs = ((i * i * i) + (ea * i) + eb) % ep
    #         if lhs == rhs:
    #             points.append(str(i) + ',' + str(j))
    # points.append(eO)
    #
    #
    # def valid(P):
    #     if P == eO:
    #         return True
    #     else:
    #         return (
    #                 (P.y ** 2 - (P.x ** 3 + ea * P.x + eb)) % ep == 0 and
    #                 0 <= P.x < ep and 0 <= P.y < ep)
    #
    #
    # def inv_mod_p(x):
    #     if x % ep == 0:
    #         raise ZeroDivisionError("Impossible inverse")
    #     return pow(x, ep - 2, ep)
    #
    #
    # def ec_inv(P):
    #     if P == eO:
    #         return P
    #     return Point(P.x, (-P.y) % ep)
    #
    #
    # def ec_add(P, Q):
    #     if not (valid(P) and valid(Q)):
    #         raise ValueError("Invalid inputs")
    #
    #     if P == eO:
    #         result = Q
    #     elif Q == eO:
    #         result = P
    #     elif Q == ec_inv(P):
    #         result = eO
    #     else:
    #         if P == Q:
    #             dydx = (3 * P.x ** 2 + ea) * inv_mod_p(2 * P.y)
    #         else:
    #             dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
    #         x = (dydx ** 2 - P.x - Q.x) % ep
    #         y = (dydx * (P.x - x) - P.y) % ep
    #         result = Point(x, y)
    #
    #     assert valid(result)
    #     return result
    #
    #
    # nat = k * enb
    # if epb == eO:
    #     P = Q = eO
    # else:
    #     xp = xq = int(eg.split(',')[0])
    #     yp = yq = ep - int(eg.split(',')[1])
    #     P = Point(xp, yp)
    #     Q = Point(xq, yq)
    # if nat == 1:
    #     nbkg = eg
    # else:
    #     while nat != 1:
    #         r = ec_add(P, Q)
    #         if r == eO:
    #             P = r
    #         else:
    #             xp = r.x
    #             yp = r.y
    #             P = Point(xp, yp)
    #         nat = nat - 1
    #     if r == eO:
    #         nbkg = r
    #     else:
    #         nbkg = str(xp) + ',' + str(yp)
    #
    # bina = ''
    # ct = []
    # for i in ct1:
    #     ct.append(points[radix.index(i)])
    # for ok in ct:
    #     if ok == eO:
    #         P = eO
    #     else:
    #         t = ok.split(',')
    #         P = Point(int(t[0]), int(t[1]))
    #     if nbkg == eO:
    #         Q = eO
    #     else:
    #         Q = Point(int(nbkg.split(',')[0]), int(nbkg.split(',')[1]))
    #     r = ec_add(P, Q)
    #     if r == eO:
    #         ct[ct.index(ok)] = points.index(eO)
    #     else:
    #         xp = r.x
    #         yp = r.y
    #         ct[ct.index(ok)] = points.index(str(xp) + ',' + str(yp))
    # for i in ct:
    #     bina = bina + format(i, '06b')
    # if len(bina) % 8 != 0:
    #     for i in range((8 - (len(bina) % 8))):
    #         bina = bina + str(0)
    # bina.replace('0b', '')
    # i = 0
    # ct = []
    # while (i != len(bina)):
    #     t = bina[i:i + 8]
    #     t = '0b' + t
    #     t = int(t, 2)
    #     ct.append(chr(t))
    #     i = i + 8
    #
    # pt1 = ''.join(ct)
    # pt1 = pt1.rstrip('\x00')
    # print('Decrypted Text =', pt1)
    #
    # message = ""
    # y = open('dehex_output.txt', 'r')
    # for line in y:
    #     message = message + line

    final_number_list = [x for x in pt1]
    final_number_arr = numpy.array(final_number_list)
    print(" Array format of Encrypted Text : ", final_number_arr)

    # Step 2
    result = []
    for elem in final_number_arr:
        result.extend(ord(num) for num in elem)
    new_list_ascii = numpy.array(result)
    print(" ASCII Value of Encrypted array : ", new_list_ascii)

    # Step 3
    # encrypt_key1 = str(encrypt_key)

    # message1 = encryption_key
    # message1 = ""
    # inputFile = open(encryption_key, 'r')
    # for line in inputFile:
    # message1 = message1 + line
    message1 = message1.strip()
    message1 = message1.rstrip(']')
    message1 = message1.lstrip('[')
    message1 = message1.replace(" ", "")
    message1 = "".join(message1.splitlines())
    print(message1)

    encrypt_key_list = [x for x in message1]
    print(encrypt_key_list)
    key_array = [int(x) for x in encrypt_key_list]

    encrypt_key_arr = numpy.array(key_array)
    print(encrypt_key_arr)

    # key_array = [int(x) for x in encrypt_key_arr]
    print(" Key as Array format ", encrypt_key_arr)

    # Step 4
    encrypt_key_length = len(key_array)
    print(" The key size is : ", encrypt_key_length)

    # Step 4.1
    encrypt_text_length = len(encrypted_output)
    print("Text Length is : ", encrypt_text_length)

    # Step 5
    quotient = int(encrypt_text_length / encrypt_key_length)

    # Step 6
    reshaped_ASCII_array = new_list_ascii.reshape(quotient, encrypt_key_length)

    # Step 7
    final_dec = []
    final_dec = reshaped_ASCII_array - encrypt_key_arr

    # Step 8
    final_dec = numpy.array(final_dec).flatten()
    print(final_dec)

    # Step 9
    final_1_enc = "".join([chr(c) for c in final_dec])
    print(final_1_enc)

if encrypt_key_from_cloud == sha_decryption:
    print("Key is Matching, Decryption Starts : ")
    val = ECC_Decryption()


else:
    print("Key Mismatching, Quiting.... : ")