import random
import numpy

def findRandom():
    # Generate the random number
    num = random.randint(0, 1)

    # Return the generated number
    return num

def generateBinaryString(N):
    # Stores the empty string
    S = ""
    # Iterate over the range [0, N - 1]
    for i in range(N):
        # Store the random number
        x = findRandom()
        # Append it to the string
        S += str(x)
    # Print the resulting string
    return S


#Step 1 to get a seed number from user:
print("Welcome!")
seed_number = int(input("Enter a number:")) #step 1
# if seed number
if seed_number == 0:
    seed_number += random.randint(1, 4)
    seed_number = seed_number*5
if seed_number == 1 or seed_number == 2 or seed_number == 3 or seed_number == 4:
    seed_number = seed_number*5
else:
    seed_number = seed_number

# Make seed number even if the entered value is odd:
if seed_number % 2 == 1:
    seed_number += 1
else:
    seed_number
print(seed_number)
choice_1 = random.randint(1,2)
print(choice_1)
if choice_1 == 1: #Binary generation
    val = generateBinaryString(seed_number)
    print(val)

else: #hexadecimal
    hex1 = random.getrandbits(seed_number)
    Hex_array = numpy.array(hex(hex1)[2:])
    print("Hex array is:", Hex_array)
    val = Hex_array.tolist()

