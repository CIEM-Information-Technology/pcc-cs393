# Week 6 Assignment

> While many of the exercises in this chapter can be solved with lists or if statements, most (or even all) of them have solutions that are well suited to dictionaries. As a result, you should use dictionaries to solve all of these exercises instead of (or in addition to) using the Python features that you have been introduced to previously.

### Question 1

Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value. The function will take the dictionary and the value to search for as its only parameters. It will return a (possibly empty) list of keys from the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise. Your program should create a dictionary and then show that the reverseLookup function works correctly when it returns multiple keys, a single key, and no keys. Ensure that your main program only runs when the file containing your solution to this exercise has not been imported into another program.

### Question 2

In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that simulates rolling a pair of six-sided dice. Your function will not take any parameters. It will return the total that was rolled on two dice as its only result. Write a main program that uses your function to simulate rolling two six-sided dice 1,000 times. As your program runs, it should count the number of times that each total occurs. Then it should display a table that summarizes this data. Express the frequency for each total as a percentage of the number of rolls performed. Your program should also display the percentage expected by probability theory for each total. Sample output is shown below.

![Image.png](https://res.craft.do/user/full/2b3a56b1-74dc-b40a-d762-495c4f6c4398/doc/5182E6D8-037D-4DD9-BE75-3C9910A4E869/F94A213F-4804-4315-97EE-34FD66D48F9D_2/xopRH8z8yfMFVlPmlsuTHS7UUYOdwxCpUMYDBkrtdM4z/Image.png)

### Question 3

Morse code is an encoding scheme that uses dashes and dots to represent digits and letters. In this exercise, you will write a program that uses a dictionary to store the mapping from these symbols to Morse code. Use a period to represent a dot, and a hyphen to represent a dash. The mapping from characters to dashes and dots is shown in the table below.

Your program should read a message from the user. Then it should translate all of the letters and digits in the message to Morse code, leaving a space between each sequence of dashes and dots. Your program should ignore any characters that are not listed in the previous table. The Morse code for Hello, World! is shown below:

`.... . .-.. .-.. --- .-- --- .-. .-.. -..`

![Image.png](https://res.craft.do/user/full/2b3a56b1-74dc-b40a-d762-495c4f6c4398/doc/5182E6D8-037D-4DD9-BE75-3C9910A4E869/8ECAF8E1-5039-452B-8199-09FBBFA19D28_2/U8cNesPy7natRcHn71Z38L8sCAxKvkxpnoktwx1p57wz/Image.png)

### Question 4

Create a program that determines and displays the number of unique characters in a string entered by the user. For example, Hello, World! has 10 unique characters while zzz has only one unique character. Use a dictionary or set to solve this problem.

### Question 5

Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one “e”, one “i”, one “l”, and one “v”. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.

