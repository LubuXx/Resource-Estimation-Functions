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
    """Spherical model with nugget effect C0 and range a"""
    if h == 0:
<<<<<<< HEAD:Variogram Modelling/Variogram Modelling.py
        return C0
=======
        return C0 
>>>>>>> 10765bc54f116870a3bd937030e4aa38a20590f6:Variogram Modelling.py

    elif h <= a:
        return C0 + C * ((1.5 * (h / a)) - 0.5 * (h / a) ** 3)

    else:
        return C0 + C 

<<<<<<< HEAD:Variogram Modelling/Variogram Modelling.py
C = sample_variance(data, sample_mean(data))  # sill value
a = int(input('Enter range (a): ')) # range
C0 = float(input('Enter nugget effect (C0): ')) # nugget effect

lags = list(range(0, int(input("Enter maximum lag distance: ")) + 1))
=======

C = sample_variance(data, sample_mean(data))  # sill value
a = int(input('Enter range:')) # range
C0 = float(input('Enter nugget effect:'))  # nugget effect
>>>>>>> 10765bc54f116870a3bd937030e4aa38a20590f6:Variogram Modelling.py

lags = list(range(0, 6))
exp_variogram = [variogram(data, h) if h != 0 else 0 for h in lags]
theoretical_variogram = [spherical_model(C, a, C0, h) for h in lags]

<<<<<<< HEAD:Variogram Modelling/Variogram Modelling.py
plt.figure(figsize=(max(8, len(lags) * 1.2), 5))
=======
plt.figure(figsize=(10, 5))
>>>>>>> 10765bc54f116870a3bd937030e4aa38a20590f6:Variogram Modelling.py
plt.plot(lags, exp_variogram, marker='o', label='Experimental Variogram', color='b')
plt.plot(lags, theoretical_variogram, marker='s', linestyle='--', label='Spherical Model', color='r')

plt.axhline(y=C + C0, color='gray', linestyle=':', label='Sill (C + C₀)')
plt.axhline(y=C0, color='orange', linestyle=':', label='Nugget (C₀)')
plt.axvline(x=a, color='green', linestyle=':', label='Range (a)')

<<<<<<< HEAD:Variogram Modelling/Variogram Modelling.py
plt.xlim(0, max(lags) + 1)
plt.ylim(0, max(C + C0, max(exp_variogram)) + 2)
plt.yticks(range(0, int(max(C + C0, max(exp_variogram))) + 3, 1))
=======
plt.xlim(0, a + 2)
plt.ylim(0, int(C0) + 11)               
plt.yticks(range(0, int(C0) + 12, 1))
>>>>>>> 10765bc54f116870a3bd937030e4aa38a20590f6:Variogram Modelling.py

plt.title("Experimental vs. Spherical Variogram")
plt.xlabel("Lag Distance (h)")
plt.ylabel("γ(h)")
plt.legend()
plt.grid(True)
plt.show()
