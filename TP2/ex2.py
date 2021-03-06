import numpy
import math
from PIL import Image


def signal_to_noise(arr, axis=0, ddof=0):
    arr = numpy.asanyarray(arr)
    me = arr.mean(axis=axis)
    sd = arr.std(axis=axis)
    return numpy.where(sd == 0, 0, me/sd)


def PSNR(original, compressed):
    mse = numpy.mean((original - compressed) ** 2)
    if mse == 0:
        return 100

    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr


def ex2():
    while True:
        filename_1 = input("Write an image's file name or 'exit' to close the app: ")

        if filename_1.lower() == "exit":
            break

        try:
            file_1 = open(filename_1, "rb")

        except FileNotFoundError:
            print("Wrong file or file path\n")
            continue

        image_1 = Image.open(file_1)
        image_sequence_1 = image_1.getdata()
        image_array_1 = numpy.array(image_sequence_1)

        filename_2 = input("Write another image's file name: ")

        if filename_2.lower() == "exit":
            break

        try:
            file_2 = open(filename_2, "rb")

        except FileNotFoundError:
            print("Wrong file or file path\n")
            continue

        image_2 = Image.open(file_2)
        image_sequence_2 = image_2.getdata()
        image_array_2 = numpy.array(image_sequence_2)

        image_array_e256 = []
        image_array_e256_2d = [[]]

        n_col = image_1.size[0]

        col = 0
        line = 0
        i = 0

        for a in image_array_1:
            if col == n_col:
                image_array_e256_2d.append([])
                col = 0
                line += 1

            image_array_e256.append([])

            image_array_e256[i].append((image_array_1[i][0] - image_array_2[i][0]) % 256)
            image_array_e256[i].append((image_array_1[i][1] - image_array_2[i][1]) % 256)
            image_array_e256[i].append((image_array_1[i][2] - image_array_2[i][2]) % 256)

            image_array_e256_2d[line].append([])

            image_array_e256_2d[line][col].append((image_array_1[i][0] - image_array_2[i][0]) % 256)
            image_array_e256_2d[line][col].append((image_array_1[i][1] - image_array_2[i][1]) % 256)
            image_array_e256_2d[line][col].append((image_array_1[i][2] - image_array_2[i][2]) % 256)

            col += 1
            i += 1

        array_e256 = numpy.array(image_array_e256_2d, numpy.ubyte, ndmin=3)
        image_e256 = Image.fromarray(array_e256)
        image_e256.save("e256.png")

        snr_each_component = signal_to_noise(image_array_e256)
        snr_all_components = snr_each_component.mean(0)

        print()
        print("Signal to noise ratio for each component: ", snr_each_component)
        print("Signal to noise ratio for the 3 components: ", snr_all_components)
        print("Peak signal to noise ratio: ", PSNR(image_array_1, image_array_2), '\n')


