import numpy as np
exit = False
while(exit == False):
    filename = input("Write exit to close the app or the file name to continue: ")
    if(filename == "exit" or filename == "Exit" or filename == "EXIT" ):
        exit = True
        break
    else:
        entropy = 0
        f = open(filename, "r")
        words = f.read().split()
        f.close()
        words = [int(x) for x in words]
        unique = []
        for x in words:
            if x not in unique:
                unique.append(x)
            
        wordsList = np.tolist(words)
        
        for y in unique:
            numberOfOcc = wordsList.count(y)
            entropy += (numberOfOcc/256) * math.log(1/(numberOfOcc/256),2)
            
        print(entropy)
            
            