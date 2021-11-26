import math


def ex1():
    while True:
        filename = input("Write the file name or 'exit' to close the app: ")

        if filename.lower() == "exit":
            break

        else:
            entropy1o = 0
            entropy2o = 0

            n_bytes = 0
            byte_sequence = []
            occurrences = [0] * 256

            file = open(filename, "rb")

            byte = file.read(1)
            while byte:
                byte_sequence.append(byte)
                occurrences[int.from_bytes(byte, 'big')] += 1
                n_bytes += 1
                byte = file.read(1)

            file.close()

            for idx, x in enumerate(occurrences):
                p = x / n_bytes

                if p > 0:
                    entropy1o -= p * math.log(p, 2)

                    if idx > 0:
                        entropy2o -= occurrences[idx-1] / n_bytes * p * math.log(p, 2)
                    else:
                        entropy2o -= p * math.log(p, 2)

            print(byte_sequence)
            print(occurrences)
            print(n_bytes)
            print(f"entropia 1ª ordem: {entropy1o}")
            print(f"entropia 2ª ordem: {entropy2o}")
