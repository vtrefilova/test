from numpy import sign
from random import randint, random


def random_array(n):
    result = []
    # Array consisting of random non-matching integers:
    random_length = [randint(i * 20 + 1, (i + 1) * 20) for i in range(int(n))]
    for i in range(int(n)):
        # Array of length = random_length[i] consisting of random numbers:
        random_arr = [random() for j in range(random_length[i])]
        # Sorting the random_arr:
        if random_length[i] % 2 == 0:
            random_arr.sort()
        else:
            random_arr.sort(reverse=True)
        result.append(random_arr)
    return result


# Checking if the input number is natural:
while True:
    num = input("Please enter a natural number ")
    try:
        val = int(num)
        if sign(val) == 1 and val % 1 == 0:
            print('result =', random_array(val))
            break
        else:
            print("This is not a natural number. Please enter a valid number")
    except ValueError:
        try:
            val = float(num)
            if sign(val) == 1 and val % 1 == 0:
                print('result =', random_array(val))
                break
            else:
                print("This is not a natural number. Please enter a valid number")
        except ValueError:
            print("This is not a number. Please enter a valid number")
