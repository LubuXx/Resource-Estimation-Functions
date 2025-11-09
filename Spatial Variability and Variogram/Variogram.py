import matplotlib.pyplot as plt

# The distance between nearby data is 1 meter.
data_set_1 = [2, 4, 6, 16, 18, 12, 10, 20, 14]
data_set_2 = [10, 14, 20, 16, 12, 6, 4, 18, 2]

# Variogram Function:
def sample_mean(data):
    return sum(data) / len(data)

def standard_deviation(data, mean):
    total = sum((i - mean) ** 2 for i in data)
    return (total / (len(data) - 1)) ** 0.5

def variogram(data, distance):
    total = 0
    n = len(data)

    for i in range(n - distance):
        total += (data[i] - data[i + distance]) ** 2

    return total / (2 * (n - distance))

lags = list(range(1, 6))

variograms_1 = [variogram(data_set_1, h) for h in lags]
variograms_2 = [variogram(data_set_2, h) for h in lags]

# Graph Settings:
plt.figure(figsize=(8, 5))
plt.plot(lags, variograms_1, marker='o', label='Data Set 1', color='b')
plt.plot(lags, variograms_2, marker='s', label='Data Set 2', color='r')
plt.ylim(18,42)
plt.yticks(range(18, 42, 3))

plt.xlim(min(lags), max(lags))
plt.ylim(min(min(variograms_1), min(variograms_2)) - 1, max(max(variograms_1), max(variograms_2)) + 1)

plt.title("Experimental Variogram (h = 1–5)")
plt.xlabel("Lag Distance (h)")
plt.ylabel("γ(h)")
plt.legend()
plt.grid(True)
plt.show()