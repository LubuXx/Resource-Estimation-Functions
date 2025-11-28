import numpy as np

# Örnek gamma fonksiyonu (spherical veya herhangi bir model)
def gamma(h):
    return h  # buraya istediğin varyogram modelini koyacaksın

# Noktalar
x1 = 0.0
x2 = 10.0
x0 = 4.0   # tahmin edilen nokta

# Mesafeler
h11 = abs(x1 - x1)
h12 = abs(x1 - x2)
h21 = abs(x2 - x1)
h22 = abs(x2 - x2)

h10 = abs(x1 - x0)
h20 = abs(x2 - x0)

# A matrisi (kriging coefficient matrix)
A = np.array([
    [gamma(h11), gamma(h12), 1],
    [gamma(h21), gamma(h22), 1],
    [1,          1,          0]
])

# b vektörü
b = np.array([
    gamma(h10),
    gamma(h20),
    1
])

print("A matrisi:")
print(A)

print("\nb vektörü:")
print(b)

# λ1, λ2, μ çözümü
solution = np.linalg.solve(A, b)
lambda1, lambda2, mu = solution

print("\nÇözüm:")
print(f"λ1 = {lambda1}")
print(f"λ2 = {lambda2}")
print(f"μ  = {mu}")
