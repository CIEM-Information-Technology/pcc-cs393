from question_3 import proper_divisor


def perfect_number(n: int):
    if sum(proper_divisor(n)) == n:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Perfect numbers within 1 and 10,000 are - ")
    for i in range(10000):
        if perfect_number(i):
            print(f"{i}  ", end="")
