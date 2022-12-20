import random


def generateOtp(n):
    min = 0
    max = 9
    output = ""
    for e in range(n):
        number = random.randint(min, max)
        output += str(number)
    return output