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

        # Calculate 1st order entropy
        entropy1o = 0
        most_frequent_symbol = -1
        most_frequent_p = 0.0

        for symbol in symbol_occurrences:
            p = symbol_occurrences[symbol] / n_bytes

            if p > 0:
                symbol_probability[symbol] = p
                entropy1o -= p * math.log(p, 2)

                if p > most_frequent_p:
                    most_frequent_p = p
                    most_frequent_symbol = symbol

        # Calculate smallest sub group with higher than 50% probability
        group = []
        group_probability = 0.0

        while group_probability < 0.5:
            max_p = 0.0
            sy = -1

            for symbol in symbol_probability:
                if symbol not in group and symbol_probability[symbol] > max_p:
                    max_p = symbol_probability[symbol]
                    sy = symbol

            group.append(sy)
            group_probability += max_p

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

        # Print results
        print(f"1.a")
        print(f"entropia 1ª ordem: {entropy1o} bits/symbol")
        print(f"maior frequência de ocorrência: simbolo \"{most_frequent_symbol}\" com {most_frequent_p*100}%\n")

        print(f"1.b")
        print(f"menor sub-grupo com frequência de ocorrência > 50%: {group}\n")

        print(f"1.c")
        print(f"entropia 2ª ordem: {entropy2o} bits/symbol\n")
