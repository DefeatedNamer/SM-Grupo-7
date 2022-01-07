import math


def ex2():
    while True:
        filename = input("Write the file name or 'exit' to close the app: ")

        if filename.lower() == "exit":
            break

        try:
            file = open(filename, "rb")

        except FileNotFoundError:
            print("Wrong file or file path\n")
            continue

        # Declare Variables
        n_bytes = 0
        symbol_sequence = []

        symbol_occurrences = {}
        symbol_probability = {}

        # Read file
        symbol = file.read(1)
        while symbol:
            symbol = int.from_bytes(symbol, 'big')
            n_bytes += 1

            symbol_sequence.append(symbol)

            if symbol in symbol_occurrences:
                symbol_occurrences[symbol] += 1
            else:
                symbol_occurrences[symbol] = 1

            symbol = file.read(1)

        file.close()

        for symbol in symbol_occurrences:
            p = symbol_occurrences[symbol] / n_bytes

            if p > 0:
                symbol_probability[symbol] = p

        # Calculate 1st order Markov model entropy
        markov_entropy_1o = 0

        n_transitions = 0
        transitions = []

        transition_occurrences = {}
        transition_probability = {}

        for idx, symbol in enumerate(symbol_sequence):
            if idx < len(symbol_sequence) - 1:
                t = (symbol, symbol_sequence[idx + 1])
                transitions.append(t)
                n_transitions += 1

                if t in transition_occurrences:
                    transition_occurrences[t] += 1
                else:
                    transition_occurrences[t] = 1

        for t in transition_occurrences:
            p = transition_occurrences[t] / symbol_occurrences[t[0]]

            if p > 0:
                transition_probability[t] = p
                h = -(symbol_probability[t[0]] * p * math.log(p, 2))
                markov_entropy_1o += h

        m1_max = 0
        m1_min = 256

        for s in symbol_occurrences:
            if symbol_probability[s] > 0:
                p = 0

                for t in transition_occurrences:
                    if t[0] == s:
                        t_prob = transition_probability[t]
                        p -= t_prob * math.log(t_prob, 2)

                if p > 0:
                    if p > m1_max:
                        m1_max = p

                    if p < m1_min:
                        m1_min = p

        # Print results
        print(f"2")
        print(f"entropia Markov 1ª ordem: {markov_entropy_1o} bits/symbol")
        print(f"entropia Markov 1ª ordem min: {m1_min} bits/symbol")
        print(f"entropia Markov 1ª ordem max: {m1_max} bits/symbol\n")