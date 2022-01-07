import random


def ex3(p, n):

    if p > 1 or p < 0:
        return

    sequence = []

    if n > 0:
        sequence.append(random.randint(0, 255))

    for i in range(n):
        rand_percent = random.random()
        print(f"{rand_percent}\n")
        next_symbol = 0

        if p > 0 and rand_percent <= p/3:
            next_symbol = sequence[i] - 1

        elif p > 0 and rand_percent <= (p/3)*2:
            next_symbol = sequence[i]

        elif p > 0 and rand_percent <= p:
            next_symbol = sequence[i] + 1

        elif rand_percent <= p + (1-p)/4:
            next_symbol = sequence[i] - 3

        elif rand_percent <= p + ((1-p)/4)*2:
            next_symbol = sequence[i] - 2

        elif rand_percent <= p + ((1-p)/4)*3:
            next_symbol = sequence[i] + 2

        else:
            next_symbol = sequence[i] + 3

        sequence.append(next_symbol % 256)

    print(sequence)



