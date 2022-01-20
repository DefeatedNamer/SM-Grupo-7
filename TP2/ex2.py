import numpy
from PIL import Image


def signal_to_noise(arr, axis=0, ddof=0):
    arr = numpy.asanyarray(arr)
    me = arr.mean(axis)
    sd = arr.std(axis=axis, ddof=ddof)
    return numpy.where(sd == 0, 0, me/sd)


def ex2():
    image = Image.open("kodim10.png")

    image_sequence = image.getdata()
    image_array = numpy.array(image_sequence)

    print(image_array)
    print("Signal to noise ratio for array1: ", signal_to_noise(image_array, axis=0, ddof=0))
