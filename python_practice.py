# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input an integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX
input variable N from user
create fibonacci sequence
label each number in fibonacci sequence as the Nth number
while i < N+1th number
    add N to total
    end when i = N+1
return total to user
"""
from pandas.core.arrays import numpy_

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 1 # what Nth number of the fibonacci sequence the loop is on (need to start at 1, not 0)
total = 0 # addition total that will be returned to user

while count < N: # while the Nth number is less than the N the user provided
    total = total + b # add fibonacci number to total

    next_value = a + b # create next number in fibonacci sequence (addition of two previous numbers)
    a = b # shift a and b to next two fibonacci numbers
    b = next_value

    count += 1 # shift count to next Nth number

print(total) # return total to user

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
N = 9
fib_seq = [0,1]
a = 0
b = 1
i = 1

while i < N:
    next_value = a + b
    fib_seq.append(next_value)
    a = b
    b = next_value
    i += 1

import numpy as np # google AI helped me with this syntax and for np.std() below
print("Standard deviation of fibonacci sequence = " + str(np.std(fib_seq)))

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def sum_fib_seq(N):
    a = 0
    b = 1  # set b to the second fibonacci number
    count = 1  # what Nth number of the fibonacci sequence the loop is on (need to start at 1, not 0)
    total = 0  # addition total that will be returned to user
    while count < N:  # while the Nth number is less than the N the user provided
        total = total + b  # add fibonacci number to total
        next_value = a + b  # create next number in fibonacci sequence (addition of two previous numbers)
        a = b  # shift a and b to next two fibonacci numbers
        b = next_value
        count += 1  # shift count to next Nth number
    return total

fib_list = [sum_fib_seq(5), sum_fib_seq(10), sum_fib_seq(15), sum_fib_seq(20), sum_fib_seq(25), sum_fib_seq(30)]
print(fib_list)
# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = "0"
    b = "1"

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total = b
        a, b = b, a + b
    return total


# Add your test cases here

# %%
