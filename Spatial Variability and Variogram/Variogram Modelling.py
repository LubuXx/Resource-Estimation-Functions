from data_storage import list_datasets, get_dataset
from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

list_datasets()
dataset_name = input("Enter the name of dataset that you want to use: ")

data = get_dataset(dataset_name)
if data is None:
    raise ValueError("❌ Incorrect of the dataset name.")

data = np.array(data, dtype=float)
n = len(data)

max_lag = int(input("Enter maximum lag distance (integer): "))

pairs = list(combinations(range(n), 2))
h_all = np.array([abs(i-j) for i, j in pairs], dtype=float)
gamma_all = np.array([0.5 * (data[i] - data[j])**2 for i, j in pairs])

lags = np.arange(1, max_lag + 1)
gamma_exp, N_pairs = [], []

for lag in lags:
    mask = (h_all == lag)
    if np.any(mask):
        gamma_exp.append(np.mean(gamma_all[mask]))
        N_pairs.append(np.sum(mask))

    else:
        gamma_exp.append(np.nan)
        N_pairs.append(0)

gamma_exp = np.array(gamma_exp)
N_pairs = np.array(N_pairs)

def spherical_gamma(h, C0, C, a):
    h = np.asarray(h, dtype=float)
    gamma = np.empty_like(h)
    hr = h / a
    mask = h <= a
    gamma[mask] = C0 + C * (1.5 * hr[mask] - 0.5 * hr[mask]**3)
    gamma[~mask] = C0 + C

    return gamma

C0_vals = np.linspace(0.0, 2.0, 41)
C_vals  = np.linspace(0.1, 15.0, 149)
a_vals  = np.linspace(1.0, 9.0, 81)

best_sse = np.inf
best_params = None

for C0 in C0_vals:
    for C in C_vals:
        for a in a_vals:
            model = spherical_gamma(lags, C0, C, a)
            mask_valid = N_pairs > 0
            sse = np.sum(N_pairs[mask_valid] * (gamma_exp[mask_valid] - model[mask_valid])**2)

            if sse < best_sse:
                best_sse = sse
                best_params = (C0, C, a)

C0_fit, C_fit, a_fit = best_params

df = pd.DataFrame({
    'Lag': lags,
    'Experimental γ(h)': np.round(gamma_exp, 4),
    'Pairs': N_pairs
})

print("\n📊 WLS Results (Spherical Model)")
print("------------------------------------")
print(f"C₀ (Nugget) = {C0_fit:.3f}")
print(f"C  (Sill)   = {C_fit:.3f}")
print(f"a  (Range)  = {a_fit:.3f}")
print(f"Weighted SSE = {best_sse:.6e}")
print("\nExperimental Values:\n")
print(df.to_string(index=False))

if C0_fit == 0:
    model_type = "Spherical Model"

else:
    model_type = "Nested Structure Model"

h_plot = np.linspace(0, max_lag, 200)
gamma_fit = spherical_gamma(h_plot, C0_fit, C_fit, a_fit)

y_max = max(np.nanmax(gamma_exp), C_fit + C0_fit) + 3
x_max = max_lag + 2

plt.figure(figsize=(8, 5))
plt.plot(lags, gamma_exp, 'o', label='Experimental γ(h)', color='b')
plt.plot(h_plot, gamma_fit, '-', label=f'{model_type}\nC₀={C0_fit:.2f}, C={C_fit:.2f}, a={a_fit:.2f}', color='r')

plt.axhline(y=C_fit + C0_fit, color='gray', linestyle=':', label='Sill (C + C₀)')
plt.axhline(y=C0_fit, color='orange', linestyle=':', label='Nugget (C₀)')
plt.axvline(x=a_fit, color='green', linestyle=':', label='Range (a)')

plt.xlim(0, x_max)
plt.ylim(0, y_max)
plt.title(f"Experimental and {model_type} Variogram Graph\n({dataset_name})")
plt.xlabel("Lag Distance (h)")
plt.ylabel("Semivariance γ(h)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()