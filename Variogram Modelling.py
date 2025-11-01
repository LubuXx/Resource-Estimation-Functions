import matplotlib.pyplot as plt

# The distance between nearby data is 1 meter. The sill value (C) is sample variance.
# The experimental model fits with spherical model.
data = [2, 3, 3, 7, 7, 7, 7, 9, 9]

def sample_mean(data):
    return sum(data) / len(data)

def sample_variance(data, mean):
    total = sum((i - mean) ** 2 for i in data)
    return total / (len(data) - 1)

def variogram(data, distance):
    total = 0
    n = len(data)

    for i in range(n - distance):
        total += (data[i] - data[i + distance]) ** 2

    return total / (2 * (n - distance))

def spherical_model(C, a, C0, h):
    if h == 0:
        return 0 

    elif h <= a:
        return C0 + C * ((1.5 * (h / a)) - 0.5 * (h / a) ** 3)

    else:
        return C0 + C

C = sample_variance(data, sample_mean(data)) # Sill Value
a = 4  # Range
C0 = 0  # Nugget Effect

lags = list(range(0, 6)) 

exp_variogram = [variogram(data, h) if h != 0 else 0 for h in lags]
theoretical_variogram = [spherical_model(C, a, C0, h) for h in lags]


plt.figure(figsize=(8, 5))
plt.plot(lags, exp_variogram, marker='o', label='Experimental Variogram', color='b')
plt.plot(lags, theoretical_variogram, marker='s', linestyle='--', label='Spherical Model', color='r')

plt.xlim(0, 5)
plt.ylim(0, 11)
plt.yticks(range(0, 11, 1))

plt.title("Experimental vs. Spherical Variogram")
plt.xlabel("Lag Distance (h)")
plt.ylabel("γ(h)")
plt.legend()
plt.grid(True)
plt.show()
