import random
import numpy
import secrets
from operator import xor

# Step 1 - To get a seed number from user:
print("Welcome!")
seed_number = int(input("Enter a number as input:"))

# Step 2 - Make seed number even if the entered value is odd:
if seed_number % 2 == 1:
    seed_number += 1
else:
    seed_number
print("The updated Seed Number is", seed_number)

# Step 3 - To generate random Hexadecimal Number based on the seed Number
hex_string = '0123456789abcdef'
hexadecimal_number =''.join([secrets.choice(hex_string) for x in range(seed_number)])
print(hexadecimal_number)

# Step 4 - To Generate its decimal equivalent of the Hexadecimal Number
print("The original string : " + str(hexadecimal_number))
res = int(hexadecimal_number, 16)
print("The decimal number of hexadecimal string : " + str(res))

# Step 5 - Split the hexadecimal into 2 equal halves and stored in seperate variables
print("The original string is : " + hexadecimal_number)
first_part = hexadecimal_number[0:len(hexadecimal_number)//2]
second_part = hexadecimal_number[len(hexadecimal_number)//2 if len(hexadecimal_number)%2 == 0
                                 else ((len(hexadecimal_number)//2)+1):]
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
print("The XORed of First and second part is : " +a[2:])

# Concatenating the resultant in the right of the original hexadecimal string
b = a[2:]
c = (hexadecimal_number + b)
print("The resultant of Concatenated string is : " +c)

# Step 7 - Finding the decimal equivalent of the newly generated Hexadecimal Number
print("The original string : " + str(c))
res1 = int(c, 16)
print("The decimal number of hexadecimal string : " + str(res1))

# Adding the Decimal equivalent of original and newly created hexadecimal number
final_number = res ^ res1
print("The Number is :" ,final_number)

