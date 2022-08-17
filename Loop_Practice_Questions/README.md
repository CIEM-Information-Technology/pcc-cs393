# Loops Practice Questions

### Question 1

February 4, 2013 was the last day that pennies were distributed by the Royal Canadian Mint. Now that pennies have been phased out retailers must adjust totals so that they are multiples of 5 cents when they are paid for with cash (credit card and debit card transactions continue to be charged to the penny). While retailers have some freedom in how they do this, most choose to round to the closest nickel.

Write a program that reads prices from the user until a blank line is entered.

Display the total cost of all the entered items on one line, followed by the amount due if the customer pays with cash on a second line. The amount due for a cash payment should be rounded to the nearest nickel. One way to compute the cash payment amount is to begin by determining how many pennies would be needed to pay the total. Then compute the remainder when this number of pennies is divided by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust the total up.

### Question 2

Write a program that computes the perimeter of a polygon. Begin by reading the x and y coordinates for the first point on the perimeter of the polygon from the user. Then continue reading pairs of values until the user enters a blank line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the previous point and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add the distance from the last point back to the first point to the perimeter. Then the perimeter should be displayed. Sample input and output values are shown below.

```other
Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1 Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0 Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373095
```

### Question 3

Fizz-Buzz is a game that is sometimes played by children to help them learn about division. The players are commonly arranged in a circle so that the game can progress from player to player continually. The starting player begins by saying one, and then play passes to the player to the left. Each subsequent player is responsible for the next integer in sequence before play passes to the following player. On a player’s turn they must either say their number or one of following substitutions:

• If the player’s number is divisible by 3 then the player says fizz instead of their number.

• If the player’s number is divisible by 5 then the player says buzz instead of their number.

A player must say both fizz and buzz for numbers that are divisible by both 3 and 5. Any player that fails to perform the correct substitution or hesitates before answering is eliminated from the game. The last player remaining is the winner.

Write a program that displays the answers for the first 100 numbers in the Fizz- Buzz game. Each answer should be displayed on its own line.

### Question 4

One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As a result, he developed what later became known as the Caesar cipher.

The idea behind this cipher is simple (and as such, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.

The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher.

Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used both to encode messages and decode messages.

### Question 5

Write a program that implements Newton’s method to compute and display the square root of a number, x, entered by the user. The algorithm for Newton’s method follows:

```other
Read x from the user
Initialize guess to x/2
While guess is not good enough do
	Update guess to be the average of guess and x/guess
```

When this algorithm completes, guess contains an approximation of the square root of x. The quality of the approximation depends on how you define “good enough”. In the author’s solution, guess was considered good enough when the absolute value of the difference between guess ∗ guess and x was less than or equal to $10^{-12}$.

### Question 6

In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10. Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. It should also include labels down the left side consisting of the numbers 1 through 10. The expected output from the program is shown below:

![Image.png](https://res.craft.do/user/full/2b3a56b1-74dc-b40a-d762-495c4f6c4398/doc/86BFA26C-1889-4D3E-BBE5-44BB64FD828A/46FC40DD-95E4-4DD7-8D6E-89FB8E73D40F_2/DibkVPmRIgbVKfBtdrv2kfbHLyFhwHUVKem0AxGCZb8z/Image.png)

When completing this exercise you will probably find it helpful to be able to print out a value without moving down to the next line. This can be accomplished by added end="" as the last argument to your print statement. For example, print("A") will display the letter A and then move down to the next line. The statement print("A", end="") will display the letter A without moving down to the next line, causing the next print statement to display its result on the same line as the letter A.

### Question 7

This exercise examines the process of identifying the maximum value in a collection of integers. Each of the integers will be randomly selected from the numbers between 1 and 100. The collection of integers may contain duplicate values, and some of the integers between 1 and 100 may not be present.

Take a moment and think about how you would solve this problem on paper. Many people would check each integer in sequence and ask themself if the number that they are currently considering is larger than the largest number that they have seen previously. If it is, then they forget the previous maximum number and remember the current number as the new maximum number. This is a reasonable approach, and will result in the correct answer when the process is performed carefully. If you were performing this task, how many times would you expect to need to update the maximum value and remember a new number?

While we can answer the question posed at the end of the previous paragraph using probability theory, we are going to explore it by simulating the situation. Cre- ate a program that begins by selecting a random integer between 1 and 100. Save this integer as the maximum number encountered so far. After the initial integer has been selected, generate 99 additional random integers between 1 and 100. Check each integer as it is generated to see if it is larger than the maximum number encountered so far. If it is then your program should update the maximum number encountered and count the fact that you performed an update. Display each integer after you gen- erate it. Include a notation with those integers which represent a new maximum.

After you have displayed 100 integers your program should display the max- imum value encountered, along with the number of times the maximum value was updated during the process. Partial output for the program is shown below, with... representing the remaining integers that your program will display. Run your program several times. Is the number of updates performed on the maximum value what you expected?

```other
30
74 <== Update
58
17
40
37
13
34
46
52
80 <== Update
37
97 <== Update
45
55
73
...
The maximum value found was 100
The maximum value was updated 5 times
```

