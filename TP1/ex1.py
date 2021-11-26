import math


def ex1():
    while True:
        filename = input("Write the file name or 'exit' to close the app: ")

        if filename.lower() == "exit":
            break

        else:
            entropy = 0
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
            
            for y in occurrences:
                p = y / n_bytes

                if p > 0:
                    entropy -= p * math.log(p, 2)

            print(byte_sequence)
            print(occurrences)
            print(n_bytes)
            print(entropy)
