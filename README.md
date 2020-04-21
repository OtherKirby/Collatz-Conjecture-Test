# Collatz-Conjecture-Test

My simple implementation testing the Collatz Conjecture, which is 

This process will eventually reach the number 1, regardless of which positive integer is chosen initially.

The test is simple to understand, and so far impossible to prove. It has been talked about many times, so I will just copy from [wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)


 Start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1. 

 Obviously my implementation will not solve this problem for a few reasons:

 1. This implementation is in Python, and I will only do it on my personal machine, not utilizing any GPU, external performance boosters, or a more efficient programming language, and will therefore run into a `MemoryError` at some point.
 2. The purpose of this implementation is not to prove the conjecture, but rather make an attempt to visualize, represent, and analyze the problem. 

