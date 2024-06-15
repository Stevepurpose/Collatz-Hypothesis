# Collatz Algorithm
1. Take a positive integer that is not zero.
2. If even, evaluate a new C0 as C0/2.
3. Else if odd, evaluate a new C0 as 3*C0+1.
4. If C0!=1 go back to 2nd step.

In Python we an execute an else block immediately after a while loop.
We will be executing the algorithm above with that setup.

By hand we will have:
1. C0 = 5
3. 5 is odd
   c0 = c0*3+1 
   c0   = 3 * 5 + 1
   c0 = 16
4. c0 != 1, go back to 2
2. 16 is even
   c0 = 16/2 
   c0 = 8
4. c0 !=1, go back to 2
2. 8 is even.
   c0 = 8/2
   c0 = 4
4. c0 != 1, go back to 2
2. 4 is even
   c0 = 4/2
   c0 = 2
4. c0 !=1, go back to 2
2. 2 is even
   c0 = 2/2
   c0 = 1
4. c0 is equal to 1
   exit loop

Initializing c0 with 5 we had: 16, 8, 4, 2, 1. Go to the `alg.py` file to see the code. 
