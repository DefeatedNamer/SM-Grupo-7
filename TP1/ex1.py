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

            entropy1o = 0

            for idx, count in enumerate(symbol_occurrences):
                p = count / n_bytes
                symbol_probability[idx] = p

                if p > 0:
                    entropy1o -= p * math.log(p, 2)

            entropy2o = 0

            pairs = []
            pair_occurrences = {}

            for idx, byte in enumerate(byte_sequence):
                if idx < len(byte_sequence) - 1:
                    pair = (byte, byte_sequence[idx + 1])
                    pairs.append(pair)

                    if pair in pair_occurrences:
                        pair_occurrences[pair] += 1
                    else:
                        pair_occurrences[pair] = 1

            for pair in pair_occurrences:
                count = 0
                for other_pair in pair_occurrences:
                    if other_pair[0] == pair[0]:
                        count += pair_occurrences[other_pair]

                p = pair_occurrences[pair] / count

                if p > 0:
                    entropy2o -= p * math.log(p, 2)

            markov_entropy_1o = 0

            for pair in pair_occurrences:
                count = 0
                for other_pair in pair_occurrences:
                    if other_pair[0] == pair[0]:
                        count += pair_occurrences[other_pair]

                p = pair_occurrences[pair] / count

                if p > 0:
                    markov_entropy_1o -= symbol_probability[int.from_bytes(pair[0], 'big')] * p * math.log(p, 2)

            print(f"\nbyte_sequence: {byte_sequence}\n")
            print(f"pairs_array: {pair_occurrences}\n")

            print(f"symbol_occurrences: {symbol_occurrences}\n")

            print(f"n_bytes: {n_bytes}\n")

            print(f"entropia 1ª ordem: {entropy1o} bits/per symbol")
            print(f"entropia 2ª ordem: {entropy2o} bits/per symbol")
            print(f"entropia Markov 1ª ordem: {markov_entropy_1o} bits/per symbol\n")
