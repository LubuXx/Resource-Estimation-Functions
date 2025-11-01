# The distance between nearby data is 1 meter.

data_set_1 = [2, 4, 6, 16, 18, 12, 10, 20, 14]
data_set_2 = [10, 14, 20, 16, 12, 6, 4, 18, 2]

def sample_mean(data):
    total = 0

    for i in data:
        total += i

    return total / len(data)

def standard_deviation(data, mean):
    total = 0

    for i in data:
        total += (i - mean) ** 2

    return (total / (len(data) - 1)) ** 0.5

def variogram(data, distance):
    total = 0
    n = len(data)

    for i in range(n - distance):
        total += (data[i] - data[i + distance]) ** 2

    variogram = total / (2 * (n - distance))

    return variogram

print(variogram(data_set_1, 3))