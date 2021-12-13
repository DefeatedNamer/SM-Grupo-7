def calculate_error(actual, expected):
    return actual - expected


x = open('rfc7932.txt', "rb")
x = x.read()

preditor0 = 0
preditor1 = 0
preditor2 = 0
preditor3 = 0
preditor4 = 0

index = 0

# preditor 0
while index < len(x):
    preditor0 += calculate_error(x[index], 0)
    index += 1

index = 0
print(preditor0)

# preditor 1
while index < len(x):
    preditor1 += calculate_error(x[index], x[index - 1])
    index += 1

index = 0
print(preditor1)

# preditor 2
while index < len(x):
    preditor2 += calculate_error(x[index], 2 * x[index - 1] - x[index - 2])
    index += 1

index = 0
print(preditor2)

# preditor 3
while index < len(x):
    preditor3 += calculate_error(x[index], x[index-1] + x[index-2] + x[index-3])
    index += 1

index = 0
print(preditor3)

# preditor 4
while index < len(x):
    preditor4 += calculate_error(x[index], x[index-2])
    index += 1

index = 0
print(preditor4)
