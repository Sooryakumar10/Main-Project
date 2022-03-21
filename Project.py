import random
import fin as fin
import numpy
import secrets
from operator import xor
import nistrng
import time
from datetime import timedelta

# Reading input file from user
input_file = input("Enter your file name : ")
message = ""
inputFile = open(input_file, 'r')
for line in inputFile:
    message = message + line
print(message)

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
print(new_list)
print(len(new_list))

# Getting its ASCII Value for the input of each character
result = []
for elem in new_list:
    result.extend(ord(num) for num in elem)
new_list_ascii = numpy.array(result)
print(new_list_ascii)

seed_number = (int(len(new_list)/10))
print(seed_number)

# Step 1 - To get a seed number from user:
print("Welcome_dehex_algorithm!")
# seed_number = int(input("Enter a number as input:"))

start_time = time.time()
print("Start time is", start_time)

# Step 2 - Make seed number even if the entered value is odd:
if seed_number % 2 == 1:
    seed_number += 1
else:
    seed_number
print("\n The updated Seed Number is", seed_number)

# Step 3 - To generate random Hexadecimal Number based on the seed Number
hex_string = '0123456789abcdef'
hexadecimal_number = ''.join([secrets.choice(hex_string) for x in range(seed_number)])
print(hexadecimal_number)

# Step 4 - To Generate its decimal equivalent of the Hexadecimal Number
print("The original string : " + str(hexadecimal_number))
res = int(hexadecimal_number, 16)
print("The decimal number of hexadecimal string : " + str(res))

# Step 5 - Split the hexadecimal into 2 equal halves and stored in seperate variables
print("The original string is : " + hexadecimal_number)
first_part = hexadecimal_number[0:len(hexadecimal_number) // 2]
second_part = hexadecimal_number[len(hexadecimal_number) // 2 if len(hexadecimal_number) % 2 == 0
                                     else ((len(hexadecimal_number) // 2) + 1):]
print("The first part of string : " + first_part)
print("The second part of string : " + second_part)

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
print("The XORed of First and second part is : " + a[2:])

# Concatenating the resultant in the right of the original hexadecimal string
b = a[2:]
c = (hexadecimal_number + b)
print("The resultant of Concatenated string is : " + c)

# Step 7 - Finding the decimal equivalent of the newly generated Hexadecimal Number
print("The original string : " + str(c))
res1 = int(c, 16)
print("The decimal number of hexadecimal string : " + str(res1))

# Adding the Decimal equivalent of original and newly created hexadecimal number
final_number = res ^ res1
print("The Number is :", final_number)

# Getting the time taken by the algorithm
elapsed_time_secs = time.time() - start_time
msg_time = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
print(msg_time)

# Code to convert final_number(int) to array for encryption and written in an file:
final_number_str = str(final_number)
final_number_list = [int(x) for x in final_number_str]
final_number_arr = numpy.array(final_number_list)
print(final_number_arr)

with open('key.txt', 'w') as f:
    f.write(str(final_number_arr))

# How to calculate file size
size_final_number_array = len(final_number_arr)
print(size_final_number_array)





