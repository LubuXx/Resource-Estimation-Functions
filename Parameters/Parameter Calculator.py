import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import pandas as pd

data = np.array([2, 3, 3, 9, 7, 7, 7, 9, 7], dtype=float)
n = len(data)

pairs = list(combinations(range(n), 2))
h_all = np.array([abs(i-j) for i, j in pairs], dtype=float)
gamma_all = np.array([0.5 * (data[i] - data[j])**2 for i, j in pairs])

max_lag = n // 2
lags = np.arange(1, max_lag+1)
gamma_exp = []
N_pairs = []

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
    gamma[mask] = C0 + C * (1.5*hr[mask] - 0.5*hr[mask]**3)
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
    'lag': lags,
    'gamma_exp': np.round(gamma_exp, 4),
    'N_pairs': N_pairs
})

print(f"Fitted spherical variogram parameters (WLS):\nC0 = {C0_fit:.4f}, C = {C_fit:.4f}, a = {a_fit:.4f}")
print(f"Weighted SSE = {best_sse:.6e}\n")
print(df.to_string(index=False))

h_plot = np.linspace(0, max(lags), 200)
gamma_fit = spherical_gamma(h_plot, C0_fit, C_fit, a_fit)

plt.figure(figsize=(6,4))
plt.plot(lags, gamma_exp, 'o', label='Experimental γ(h)')
plt.plot(h_plot, gamma_fit, '-', label=f'Fit: C0={C0_fit:.2f}, C={C_fit:.2f}, a={a_fit:.2f}')
plt.xlabel('Lag (index units)'); plt.ylabel('Semivariance γ(h)')
plt.title('WLS fit of spherical variogram (new data)')
plt.legend(); plt.grid(True); plt.tight_layout(); plt.show()