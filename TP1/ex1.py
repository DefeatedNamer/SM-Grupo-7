import math
import numpy as np


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

exit = False
while not exit:
    filename = input("Write exit to close the app or the file name to continue: ")

    if filename == "exit" or filename == "Exit" or filename == "EXIT":
        exit = True
        break

    else:
        entropy = 0
        f = open(filename, "r")
        words = f.read()
        #words_as_bytes = str.encode(words)
        f.close()
        words = [bytes(x, 'utf8') for x in words] # encoding characters to bytes
        unique = []
        for x in words:
            if x not in unique:
                unique.append(x)
            
        wordsList = list(words)
        
        for y in unique:
            numberOfOcc = wordsList.count(y)
            entropy += (numberOfOcc/256) * math.log(1/(numberOfOcc/256), 2) # entropy calculation
        # FINAL RESULT
        print(entropy)
        print(most_frequent(wordsList))
            
            