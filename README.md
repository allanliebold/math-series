# math-series
This assignment is an introduction to Test Driven Development (TDD)

The exercise consisted of the Fibonacci and Lucas Sequence. This problem set consists of two files series.py, and test_series.py.

Test cases were created within test_series.py starting with the bases cases for these respective algorithms.
For example: If input argument is 1 or less - what is the corresponding starting condition for each sequence?
The next step in the testing process consisted of general tests of what came to be recursive function calls.
The design of series.py is reflected in the test cases developed in test_series.py.

The Fibonacci Sequence.

The desired number (n) is found by summing the numbers of the previous two indices (n-2), (n-1).
The algorithm is introduction to the concept of recurrence relations or recursion.  

A general description may be found at:
https://en.wikipedia.org/wiki/Fibonacci_number

The Lucas Numbers
This process is similiar to the Fibonacci sequence. This sequence has a different starting point and utilizes
the Fibonacci sequence (F) in its own formula F(n) = F(n-1) + F(n+1).

A general description may be found at:
https://en.wikipedia.org/wiki/Lucas_number

Finally, we created a sum_series function that accepts optional arguments. A number may be passed to the Lucas
or Fibonacci sequence depending upon its input arguments. Otherwise, it completes an iterative custom sequence
using the input arguments.

Authors:
David Franklin
Alan Liebold

