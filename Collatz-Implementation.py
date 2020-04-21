'''
The Collatz conjecture is: This process will eventually reach the number 1, 
regardless of which positive integer is chosen initially.
'''

import time as t

f = open(r'output.txt', 'w')

x = 2
buffer = 0.3
largest_sequence = []
largest_sequence_length = 0

def do_collatz(num):
    sequence = [num]
    # if number is negative, exit
    if num < 1:
        return []
    # run forever
    while num > 1:
        # if number is evem, divide by two
        if num % 2 == 0:
            num = num / 2 
        # if number is odd, multiply by three and add one
        else:
            num = 3 * num + 1 
        # add the new number to the list
        sequence.append(num)
    return sequence

while True:
    seq = do_collatz(x)
    print("CURRENT NUMBER: %s" % seq[0])
    print(seq)
    # if len(seq) > largest_sequence_length:
    #     seq = largest_sequence
    # if seq[0] % 10 == 0:
    # f.write(str(largest_sequence))
    # f.write('\n')
    t.sleep(buffer)
    x = x + 1

