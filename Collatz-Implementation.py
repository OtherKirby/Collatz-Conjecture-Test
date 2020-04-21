'''
The Collatz conjecture is: This process will eventually reach the number 1, 
regardless of which positive integer is chosen initially.
'''

import time as t
import winsound

f = open(r'output.txt', 'w')

x = 2
buffer = 0.3
frequency = 1500
duration = 100
largest_sequence = []
largest_sequence_length = 0

ADD_BUFFER = False
PLAY_SOUND = False
ADD_TO_FILE = True

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
    print("\nCURRENT NUMBER: %s" % seq[0])
    print(seq)
    if len(seq) > largest_sequence_length:
        largest_sequence_length = len(seq)
        largest_sequence = seq
        print("NEW LARGEST LENGTH REACHED %s" % largest_sequence_length)
        if PLAY_SOUND:
            winsound.Beep(frequency, duration)
        if ADD_TO_FILE:
            f.write("%s\n" % str(largest_sequence[0]))
            f.write("%s\n" % str(largest_sequence))
    if ADD_BUFFER:
        t.sleep(buffer)
    x = x + 1

