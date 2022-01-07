import math
import random


def ex7():
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

        # Read file
        symbol = file.read(1)
        while symbol:
            symbol = int.from_bytes(symbol, 'big')
            n_bytes += 1

            symbol_sequence.append(symbol)

            symbol = file.read(1)

        file.close()

        # Cut 128 byte sub-group
        start = random.randint(0, n_bytes - 1)
        l_symbols = symbol_sequence[start:start + 128]

        l_symbol_occurrences = {}
        l_symbol_probability = {}

        for symbol in l_symbols:
            if symbol in l_symbol_occurrences:
                l_symbol_occurrences[symbol] += 1
            else:
                l_symbol_occurrences[symbol] = 1

        # Calculate 1st order entropy
        entropy1o = 0

        for symbol in l_symbol_occurrences:
            p = l_symbol_occurrences[symbol] / 128

            if p > 0:
                l_symbol_probability[symbol] = p
                entropy1o -= p * math.log(p, 2)

        print(entropy1o)
