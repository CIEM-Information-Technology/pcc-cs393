# Week 3 Assignments
## Questions 
### Question 1
Create a python program that computes the average of a collection of values entered by the user. The user will enter 0 as a sentinel value to indicate that no further values will be provided. Your program should display an appropriate error message if the first value entered by the user is 0. 

**Keep in mind that the 0 at the end of the input should not be included in the average.**

### Question 2
A particular zoo determines the price of admission based on the age of the guest. Guests 2 years of age and less are admitted without charge. Children between 3 and 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission for all other guests is $23.00. 

**Create a program** that begins by reading the ages of all of the guests in a group from the user, with one age entered on each line. The user will enter a blank line to indicate that there are no more guests in the group. Then your program should display the admission cost for the group with an appropriate message. The cost should be displayed using two decimal places.

### Question 3
The greatest common divisor of two positive integers, n and m, is the largest number, d, which divides evenly into both n and m. There are several algorithms that can be used to solve this problem, including:
```
Initialize d to the smaller of m and n.
While 
    d does not evenly divide m or d does not evenly divide n 
    do
        Decrease the value of d by 1

Report d as the greatest common divisor of n and m
```
Write a program that reads two positive integers from the user and uses this algorithm to determine and report their greatest common divisor.

### Question 4
The prime factorization of an integer, n, can be determined using the following steps:
```
Initialize factor to 2
While factor is less than or equal to n do
    If 
        n is evenly divisible by factor then Conclude that factor is a factor of n Divide n by factor using floor division
    Else
    Increase factor by 1
```
Write a program that reads an integer from the user. If the value entered by the user is less than 2 then your program should display an appropriate error message. Otherwise your program should display the prime numbers that can be multiplied together to compute n, with one factor appearing on each line. For example -
```
Enter an integer (2 or greater): 72 
The prime factors of 72 are:
2
2
2 
3 
3
```
---
## Bonus Questions
### Question 1
Consider a sequence of integers that is constructed in the following manner:
```
Start with any positive integer as the only term in the sequence
While 
    the last term in the sequence is not equal to 1 
    do
        If the last term is even then
            Add another term to the sequence by dividing the last term by 2 using floor division
        Else
            Add another term to the sequence by multiplying the last term by 3 and adding 1
```


The Collatz conjecture states that this sequence will eventually end with one when it begins with any positive integer. Although this conjecture has never been proved, it appears to be true.

**Create a program** that reads an integer, n, from the user and reports all of the values in the sequence starting with n and ending with one. Your program should allow the user to continue entering new n values (and your program should continue displaying the sequences) until the user enters a value for n that is less than or equal to zero.

### Question 2
What’s the minimum number of times you have to flip a coin before you can have three consecutive flips that result in the same outcome (either all three are heads or all three are tails)? What’s the maximum number of flips that might be needed? How many flips are needed on average? In this exercise we will explore these questions by creating a program that simulates several series of coin flips.

Create a program that uses Python’s random number generator to simulate flipping a coin several times. The simulated coin should be fair, meaning that the probability of heads is equal to the probability of tails. Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes for one simulation on the same line. Then display the number of flips that were needed to reach 3 consecutive occurrences of the same outcome. When your program is run it should perform the simulation 10 times and report the average number of flips needed. Sample output is shown below:
```
H T T T (4 flips)
H H T T H T H T T H H T H T T H T T T (19 flips)
T T T (3 flips)
T H H H (4 flips)
H H H (3 flips)
T H T T H T H H T T H H T H T H H H (18 flips)
H T T H H H (6 flips)
T H T T T (5 flips)
T T H T T H T H T H H H (12 flips)
T H T T T (5 flips)
On average, 7.9 flips were needed.
```