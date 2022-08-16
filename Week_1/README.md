# Week 1 Assignment

### Question 1

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.

#### Test Your Code

- Run your program with `python indoor.py`. Type `THIS IS IT WORKSHOP` and press Enter. Your program should output `this is it workshop`.
- Run your program with `python indoor.py`. Type `50` and press Enter. Your program should output `50`.

### Question 2

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

### Question 3

Even if you haven’t studied physics (recently or ever!), you might have heard that $E=mc^2$, wherein $E$ represents energy (measured in Joules), represents mass (measured in kilograms), and $c$ represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

### Question 4

Write a program in a file called `energy_calculation.py` which can calculate the kinetic and potential energy of an object given the mass, velocity and height. $(g = 9.8$ $ms^{-2})$ (Assume that the mass is in $kg$, height is in $m$ and velocity is in $ms^{-1}$.

$$
K.E. = \frac{1}{2} \times mv^2
\\
P.E. = m \times g \times h
$$

#### I/O Format

```other
Enter mass: 1
Enter height: 20
Enter velocity: 10

Kinetic Energy: 50J
Potential Energy: 196.133J
```

### Question 5

Write a program in a file `temperature.py` to convert temperature from Celsius to Fahrenheit. Formula -

$$
\frac{C}{5} = \frac{F-32}{9}
$$

#### I/O Format

```other
Input value in C: 50
50C = 122F
```

### Bonus Questions

1. Modifying the script in **Question 5**, calculate the kinetic and potential energy of a ball of mass $0.1~kg$ half way up, thrown vertically upwards with an initial speed of $20~ms^{-1}$.
2. In a file called `fraction_add.py`, take input of two fractions and add them. Show the output in fraction format. E.g. Take `1/2` and `3/4` as inputs. The result of addition would be `10/8`. So, `10/8` should be shown as the output.
