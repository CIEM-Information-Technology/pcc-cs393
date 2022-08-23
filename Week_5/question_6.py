from random import randrange

MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6

if __name__ == '__main__':
    ticket_nums = []

    for i in range(NUM_NUMS):
        rand = randrange(MIN_NUM, MAX_NUM + 1)
        while rand in ticket_nums:
            rand = randrange(MIN_NUM, MAX_NUM + 1)

        ticket_nums.append(rand)

    ticket_nums.sort()
    print("Your random numbers are: ", end="")
    for n in ticket_nums:
        print(n, end=" ")
    print()
