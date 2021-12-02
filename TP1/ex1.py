import math


def ex1():
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

        symbol_occurrences = [0] * 256
        symbol_probability = [0.0] * 256

        # Read file
        symbol = file.read(1)
        while symbol:
            symbol = int.from_bytes(symbol, 'big')
            n_bytes += 1

            symbol_sequence.append(symbol)
            symbol_occurrences[symbol] += 1

            symbol = file.read(1)

        file.close()

        # Calculate 1st order entropy
        entropy1o = 0

        for idx, count in enumerate(symbol_occurrences):
            p = count / n_bytes

            if p > 0:
                symbol_probability[idx] = p
                entropy1o -= p * math.log(p, 2)

        # Calculate 2nd order entropy
        entropy2o = 0

        n_pairs = 0
        pairs = []

        pair_occurrences = {}
        pair_probability = {}

        for idx, symbol in enumerate(symbol_sequence):
            if idx % 2 == 0:
                if idx < len(symbol_sequence) - 1:
                    pair = (symbol, symbol_sequence[idx + 1])
                    pairs.append(pair)
                    n_pairs += 1

                    if pair in pair_occurrences:
                        pair_occurrences[pair] += 1
                    else:
                        pair_occurrences[pair] = 1

        for idx, pair in enumerate(pair_occurrences):
            p = pair_occurrences[pair] / n_pairs

            if p > 0:
                pair_probability[idx] = p
                entropy2o -= p * math.log(p, 2)

        entropy2o /= 2

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
                h = -(symbol_probability[t[0]] * p * math.log(p, 2))
                markov_entropy_1o += h

                if p < min_p:
                    min_p = p

                if p > max_p:
                    max_p = p
        min_p = 256
        max_p = 0

        

        # Print results
        # print(f"\nsymbol_sequence: {symbol_sequence}\n")
        # print(f"pairs_array: {pair_occurrences}\n")

        # print(f"symbol_occurrences: {symbol_occurrences}\n")

        print(f"n_bytes: {n_bytes}\n")

        print(f"entropia 1ª ordem: {entropy1o} bits/symbol\n")
        print(f"entropia 2ª ordem: {entropy2o} bits/symbol\n")

        print(f"entropia Markov 1ª ordem: {markov_entropy_1o} bits/symbol")

        print(f"entropia Markov 1ª ordem min: {min_p} bits/symbol")
        print(f"entropia Markov 1ª ordem max: {max_p} bits/symbol\n")
