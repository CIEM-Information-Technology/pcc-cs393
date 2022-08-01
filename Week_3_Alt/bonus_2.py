from random import randint

def coin_toss():
    r = randint(0, 1)
    outcomes = ['H', 'T']
    return outcomes[r]

def three_in_a_row():
    toss_results = []
    while True:
        if len(toss_results) < 3:
            toss_results.append(coin_toss())
        else:
            if toss_results[-1] == toss_results[-2] == toss_results[-3]:
                break
            else:
                toss_results.append(coin_toss())
    return toss_results

average_toss = 0

for i in range(1, 11):
    r = three_in_a_row()
    average_toss += len(r)
    print(f"{str(r)} ({len(r)} tosses)")

average_toss = average_toss / 10
print(f"Average {average_toss} tosses")
