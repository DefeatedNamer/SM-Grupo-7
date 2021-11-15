import math


def ex1():
    while True:
        filename = input("Write the file name or 'exit' to close the app: ")

        if filename.lower() == "exit":
            break

        else:
            entropy = 0
            bytes = []
            occurrences = [0] * 256

            file = open(filename, "rb")

            byte = file.read(1)
            while byte:
                bytes.append(byte)
                occurrences[int.from_bytes(byte, 'big')] += 1
                byte = file.read(1)

            file.close()

            for y in occurrences:
                if y != 0:
                    entropy += (y / 256) * math.log(1 / (y / 256), 2)

            print(bytes)
            print(occurrences)
            print(entropy)
