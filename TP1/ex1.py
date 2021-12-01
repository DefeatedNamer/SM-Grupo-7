import math


def ex1():
    while True:
        filename = input("Write the file name or 'exit' to close the app: ")

        if filename.lower() == "exit":
            break

        else:
            n_bytes = 0
            byte_sequence = []

            symbol_occurrences = [0] * 256
            symbol_probability = [0.0] * 256

            file = open(filename, "rb")

            byte = file.read(1)
            while byte:
                byte_sequence.append(byte)
                symbol_occurrences[int.from_bytes(byte, 'big')] += 1
                n_bytes += 1
                byte = file.read(1)

            file.close()

            # Calculate 1st order entropy
            entropy1o = 0

            for idx, count in enumerate(symbol_occurrences):
                p = count / n_bytes
                symbol_probability[idx] = p

                if p > 0:
                    entropy1o -= p * math.log(p, 2)

            # pair symbols with preceding symbols
            n_pairs = 0
            pairs = []

            pair_occurrences = {}

            for idx, byte in enumerate(byte_sequence):
                if idx < len(byte_sequence) - 1:
                    pair = (byte, byte_sequence[idx + 1])
                    pairs.append(pair)
                    n_pairs += 1

                    if pair in pair_occurrences:
                        pair_occurrences[pair] += 1
                    else:
                        pair_occurrences[pair] = 1

            # Calculate 2nd order entropy
            entropy2o = 0

            for idx, pair in enumerate(pair_occurrences):
                p = pair_occurrences[pair] / n_pairs

                if p > 0:
                    entropy2o -= p * math.log(p, 2)

            entropy2o /= 2

            # Calculate 1st order Markov model entropy
            markov_entropy_1o = 0

            min_entropy = 8
            max_entropy = 0

            for pair in pair_occurrences:
                count = symbol_occurrences[int.from_bytes(pair[0], 'big')]

                p = pair_occurrences[pair] / count

                if p > 0:
                    h = -(symbol_probability[int.from_bytes(pair[0], 'big')] * p * math.log(p, 2))
                    markov_entropy_1o += h

                    if p < min_entropy:
                        min_entropy = p

                    if p > max_entropy:
                        max_entropy = p

            print(f"\nbyte_sequence: {byte_sequence}\n")
            print(f"pairs_array: {pair_occurrences}\n")

            print(f"symbol_occurrences: {symbol_occurrences}\n")

            print(f"n_bytes: {n_bytes}\n")

            print(f"entropia 1ª ordem: {entropy1o} bits/symbol\n")
            print(f"entropia 2ª ordem: {entropy2o} bits/symbol\n")
            print(f"entropia Markov 1ª ordem: {markov_entropy_1o} bits/symbol")
            print(f"entropia Markov 1ª ordem min: {min_entropy} bits/symbol")
            print(f"entropia Markov 1ª ordem max: {max_entropy} bits/symbol\n")

