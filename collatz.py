# This program builds a mathematcal collatz sequence. If starting number (n) is 
# even, next num becomes n/2.
# However, if starting number is odd, next number is (3n + 1)
# collatz sequence for 10 is: 10, 5, 16, 8, 4, 2, 1

def collatz(starting_number):

    sequence = [starting_number]

# checks for negative starting numbers and 0

    num = starting_number

    if starting_number < 1:
        return []
    if starting_number == 1:
        return [1]

    while num != 1:
        if num % 2 == 0:
            num = num//2
            sequence.append(num)
        else:
            num = 3*num + 1
            sequence.append(num)
    return sequence


starting_number = 27
print((collatz(starting_number)))
