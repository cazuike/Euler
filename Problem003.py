highest = 600851475143 #fundamental theorem of arithmetic - n > 1 can be expressed as prime or product of primes
counter = 2
while highest != 1:
    if highest % counter == 0:
        highest = highest // counter
    else:
        counter += 1
print(counter)
