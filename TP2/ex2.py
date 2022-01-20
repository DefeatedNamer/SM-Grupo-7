import numpy
from PIL import Image


def signal_to_noise(arr, axis=0, ddof=0):
    arr = numpy.asanyarray(arr)
    me = arr.mean(axis)
    sd = arr.std(axis=axis, ddof=ddof)
    return numpy.where(sd == 0, 0, me/sd)


def ex2():
    while True:
        filename1 = input("Write an image's file name or 'exit' to close the app: ")

        if filename1.lower() == "exit":
            break

        try:
            file1 = open(filename1, "rb")

        except FileNotFoundError:
            print("Wrong file or file path\n")
            continue

        filename2 = input("Write another image's file name: ")

        if filename2.lower() == "exit":
            break

        try:
            file2 = open(filename2, "rb")

        except FileNotFoundError:
            print("Wrong file or file path\n")
            continue

        image1 = Image.open(file1)
        image_sequence1 = image1.getdata()
        image_array1 = numpy.array(image_sequence1)

        image2 = Image.open(file2)
        image_sequence2 = image2.getdata()
        image_array2 = numpy.array(image_sequence2)

        #image_array_e256
        #for i, a in enumerate(image_array1):

        print(image_array1, '\n')
        print(image_array2, '\n')

        print("Signal to noise ratio for 1st image: ", signal_to_noise(image_array1, axis=0, ddof=0))
        print("Signal to noise ratio for 2nd image: ", signal_to_noise(image_array2, axis=0, ddof=0), '\n')
