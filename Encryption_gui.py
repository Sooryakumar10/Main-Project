from tkinter import *
import os
import hashlib
import random
import smtplib
from asyncio import current_task
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy
import secrets
import time
from datetime import timedelta
from collections import namedtuple
from random import *
import pymongo as pymongo
import smtplib, ssl
import datetime
import pytz

global g
Point = namedtuple("Point", "x y")

def encryption():
    mail_id = mailaddr.get()
    input_file = inputfile.get()
    def dehex():
        # Dehex Encryption Algorithm - Round 1 Encryption Starts:
        # Reading input file from user
        from future.backports.email._encoded_words import len_b
        print(" Round 1 Encryption  : Dehex Algorithm ")
        message = ""
        inputFile = open(input_file, 'r')
        for line in inputFile:
            message = message + line

        # print(message)

        def Convert(message):
            list1 = []
            list1[:0] = message
            return list1

        message_list = Convert(message)
        new_list = []
        for elem in message_list:
            temp = elem.split(', ')
            new_list.append((temp))

        # Converting the input file into List of single characters
        # print(new_list)
        len_input = len(new_list)
        # print(len_input)

        # Getting its ASCII Value for the input of each character
        result = []
        for elem in new_list:
            result.extend(ord(num) for num in elem)
        new_list_ascii = numpy.array(result)
        # print(new_list_ascii)

        seed_number = (int(len(new_list) % 100))
        print(seed_number)

        # Step 1 - To get a seed number from user:

        # seed_number = int(input("Enter a number as input:"))

        start_time = time.time()
        # print("Start time as per machine is: ", start_time)

        # Step 2 - Make seed number even if the entered value is odd:
        if seed_number % 2 == 1:
            seed_number += 1
        else:
            seed_number
        # print("\n The updated Seed Number is", seed_number)

        # Step 3 - To generate random Hexadecimal Number based on the seed Number
        hex_string = '0123456789abcdef'
        hexadecimal_number = ''.join([secrets.choice(hex_string) for x in range(seed_number)])
        # print(hexadecimal_number)

        # Step 4 - To Generate its decimal equivalent of the Hexadecimal Number
        # print("The original string : " + str(hexadecimal_number))
        res = int(hexadecimal_number, 16)
        # print("The decimal number of hexadecimal string : " + str(res))

        # Step 5 - Split the hexadecimal into 2 equal halves and stored in seperate variables
        # print("The original string is : " + hexadecimal_number)
        first_part = hexadecimal_number[0:len(hexadecimal_number) // 2]
        second_part = hexadecimal_number[len(hexadecimal_number) // 2 if len(hexadecimal_number) % 2 == 0
                                         else ((len(hexadecimal_number) // 2) + 1):]
        # print("The first part of string : " + first_part)
        # print("The second part of string : " + second_part)

        # Step 6 - XOR Operation between the splitted hexadecimal Numbers
        hex_string1 = first_part
        hex_string2 = second_part
        first_part1 = int(hex_string1, 16)
        second_part1 = int(hex_string2, 16)
        hex_value1 = hex(first_part1)
        hex_value2 = hex(second_part1)
        hex_value1 = numpy.array(hex(first_part1))
        hex_value2 = numpy.array((hex(second_part1)))
        hex_value1 = hex_value1.tolist()
        hex_value2 = hex_value2.tolist()
        a = hex(first_part1 ^ second_part1)
        # print("The XORed of First and second part is : " + a[2:])

        # Concatenating the resultant in the right of the original hexadecimal string
        b = a[2:]
        c = (hexadecimal_number + b)
        # print("The resultant of Concatenated string is : " + c)

        # Step 7 - Finding the decimal equivalent of the newly generated Hexadecimal Number
        # print("The original string : " + str(c))
        res1 = int(c, 16)
        # print("The decimal number of hexadecimal string : " + str(res1))

        # Adding the Decimal equivalent of original and newly created hexadecimal number
        final_number = res ^ res1
        # print("The Number is :", final_number)

        # Getting the time taken by the algorithm
        elapsed_time_secs = time.time() - start_time
        msg_time = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
        # print("Ending time is:",msg_time)

        # Code to convert final_number(int) to array for encryption and written in an file:
        final_number_str = str(final_number)
        final_number_list = [int(x) for x in final_number_str]
        final_number_arr = numpy.array(final_number_list)
        print(final_number_arr)

        # How to calculate file size
        size_final_number_array = len(final_number_arr)
        # print(size_final_number_array)

        # To find remainder for padding
        remainder = int((len_input % size_final_number_array))
        # print(remainder)
        pad_size = size_final_number_array - remainder

        # Code for padding
        message = message + (' ' * pad_size)

        # Post padding
        message_list = Convert(message)
        new_list_1 = []
        for elem in message_list:
            temp = elem.split(', ')
            new_list_1.append((temp))

        # Converting the input file into List of single characters with padding spaces included
        # print(new_list_1)
        len_input_1 = len(new_list_1)
        # print(len_input_1)

        # Getting its ASCII Value for the input of each character
        result = []
        for elem in new_list_1:
            result.extend(ord(num) for num in elem)
        new_list_ascii_1 = numpy.array(result)
        # print(new_list_ascii_1)

        # Advanced Caeser cipher algorithm
        final_pad = []
        quotient = int(len_input_1 / size_final_number_array)
        new_list_ascii_1 = new_list_ascii_1.reshape(quotient, size_final_number_array)
        # final_number_arr = final_number_arr.reshape(1, (size_final_number_array*quotient))

        final_pad = new_list_ascii_1 + final_number_arr
        final_pad = numpy.array(final_pad).flatten()
        Round_1_enc = "".join([chr(c) for c in final_pad])
        # print(final_pad)
        print("Encrypted text after Dehex is:", Round_1_enc)
        xx = randint(1, 1000)
        newfilename = "key_".__add__(str(xx)).__add__(".txt")
        print(xx)
        with open(newfilename, 'w') as f:
            s = str(final_number_arr)
            f.write(s)
        # return Round_1_enc
        dehex_dict = dict()
        dehex_dict['Round_one_res'] = Round_1_enc
        dehex_dict['key_file'] = newfilename
        dehex_dict['id'] = xx
        return dehex_dict

    res_dehex = dehex()
    # with open('key.txt', 'w') as f:
    #     s = str(res_dehex.get('Key'))
    #     f.write(s)

    # Round 2 Encryption : ECC:

    def ecc(val):
        print("Round 2 Encryption")
        original = val
        eO = 'ORIGIN'
        ep = 71
        ea = 1
        eb = 3
        ena = 47
        enb = 8
        k = 30
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

        nat = ena
        xp = xq = int(eg.split(',')[0])
        yp = yq = int(eg.split(',')[1])
        P = Point(xp, yp)
        Q = Point(xq, yq)
        if ena == 1:
            epa = eg
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
                epa = r
            else:
                epa = str(xp) + ',' + str(yp)

        nat = enb
        xp = xq = int(eg.split(',')[0])
        yp = yq = int(eg.split(',')[1])
        P = Point(xp, yp)
        Q = Point(xq, yq)
        if enb == 1:
            epb = eg
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
                epb = r
            else:
                epb = str(xp) + ',' + str(yp)

        nat = k
        if k == 1:
            ekpb = epb
        else:
            if epb == eO:
                P = Q = eO
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
                    ekpb = r
                else:
                    ekpb = str(xp) + ',' + str(yp)
            else:
                xp = xq = int(epb.split(',')[0])
                yp = yq = int(epb.split(',')[1])
                P = Point(xp, yp)
                Q = Point(xq, yq)
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
                    ekpb = r
                else:
                    ekpb = str(xp) + ',' + str(yp)
        temp = original

        for i in temp:
            bina = bina + format(ord(i), '08b')
        if len(bina) % 6 != 0:
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
            if ok == eO:
                P = eO
            else:
                t = ok.split(',')
                P = Point(int(t[0]), int(t[1]))
            if ekpb == eO:
                Q = eO
            else:
                Q = Point(int(ekpb.split(',')[0]), int(ekpb.split(',')[1]))
            r = ec_add(P, Q)
            if r == eO:
                pt[pt.index(ok)] = radix[points.index(eO)]
            else:
                xp = r.x
                yp = r.y
                pt[pt.index(ok)] = radix[points.index(str(xp) + ',' + str(yp))]

        ct = ''.join(pt)
        ct1 = ct

        print("Encrypted Text After ECC : ", ct1)
        return ct1

    # Calling both functions
    output_eccdehex = ecc(res_dehex.get('Round_one_res'))

    with open('half.txt', 'w') as f:
        f.write(str(output_eccdehex))

    # Hasing the key using SHA256
    # result = hashlib.sha256(bytes("key.txt", encoding = 'utf-8'))
    # print("The hexadecimal equivalent of SHA256 is : ")
    # hashed_dehex_key = result.hexdigest()
    # print(hashed_dehex_key)

    # Establishing Connection with the cloud using MongoDB
    newfilename1 = res_dehex.get('key_file')
    result = hashlib.sha256(newfilename1.encode())
    print("The hexadecimal equivalent of SHA256 is : ")
    i = result.hexdigest()
    print(i)
    cloud_password = ""
    cloud_pswd = open('cloud_password.txt','r')
    for line in cloud_pswd:
        cloud_password = cloud_password + line
    client = pymongo.MongoClient(
        "mongodb+srv://soorya:"+cloud_password+"@cluster0.hl7ws.mongodb.net/Main?retryWrites=true&w=majority")
    # db = client.test
    rid = res_dehex.get('id')
    db = client["Main"]
    collections = db["Main"]
    current_time = datetime.datetime.now()
    post = {"_id": rid, "name": "dehex_ecc", "Encrypted information": output_eccdehex, "Key_Dehex": i,
            "Date and Time": current_time}
    collections.insert_one(post)
    print("Cloud Connection Established")

    # Creating Key Management through SMTP protocol - Mail Transfer

    pswd = ""
    input_pswd = open('Mail_password.txt','r')
    for line in input_pswd:
        pswd = pswd + line
    subject = "Security key for file stored in cloud ID: " + str(rid) + "."
    body = "This is an email with attachment sent from Python which has a security key file for encrypted file stored in Cloud whose ID is: " + str(
        rid) + ", which is uploaded on " + str(current_time) + "."
    sender_email = "dehexalgorithm@gmail.com"
    receiver_email = mail_id
    password = pswd

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = newfilename1  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    #print("Key Shared to Receiver for Decryption")
    emptylabel.config(text='Encryption successful! Data stored in cloud.', fg='red', font=('Arial', 20))


#def myfunc():
#    emptylabel.config(text = 'Encryption Success and Data Stored in Cloud...')

window=Tk()
window.title("Encryption")
window.geometry('1000x500')

label1 = Label(window,text='Enter the input file : ',fg = 'blue', font =('Arial',14))
label1.grid(row=1,column=1,padx=5,pady=10)

inputfile=StringVar()
mailaddr=StringVar()

textbox1 = Entry(window,textvariable=inputfile,fg = 'blue', font =('Arial',14))
textbox1.grid(row=1,column=2)

label2 = Label(window,text='Enter your mail id : ',fg = 'red', font =('Arial',14))
label2.grid(row=2,column=1,padx=5,pady=10)

textbox2 = Entry(window,textvariable=mailaddr,fg = 'red', font =('Arial',14))
textbox2.grid(row=2,column=2)



button1 = Button(window, command=encryption,  text='Encrypt',fg = 'black', font =('Arial',14))

button1.grid(row=4,column=3,padx=10)

emptylabel=Label(window,fg='green',font=('Arial',20))
emptylabel.grid(row=10,column=10,pady=10)

window.mainloop()

