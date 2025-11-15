"""
Suppose that we measure the thickness in the location G 
and want to estimate the average thickness value of the 
drive AB from the measured value (The G is located between 
AB drive.)
"""
# Values:
print("\nThe distance and thickness values.")
thicknessOfG = float(input('Enter the thickness of G:'))
distance1 = float(input('Enter the distance between AG:'))
distance2 = float(input('Enter the distance between GB:'))

total_distance = distance1 + distance2

# Parameters:
if total_distance != "":
    Sill = float(input('Enter the Sill Value:'))
    Nugget = float(input('Enter the Nugget Effect:'))
    Range = float(input('Enter the Range:'))

# Model:
if (Sill and Nugget and Range) != "":
    print("\nSelect a model type:")
    print("\nFor Spherical Mode, type: spherical_model")
    print("For Linear Mode, type: linear_model")
    print("----------------------------")

    model = str(input('Choose your model type given above:'))

# Computation of 𝛾ҧ(𝐴𝐵, 𝐺) with Spherical Model:
def spherical_model(C, C0, a, d1, d2, td):
    if C == 1:
        if d1 <= a:
            model1 = (3*d1/(2*a)) - 0.5*(d1/a)**3
        else:
            model1 = 1

        if d2 <= a:
            model2 = (3*d2/(2*a)) - 0.5*(d2/a)**3
        else:
            model2 = 1

        return C0 + C * ((d1/td)*model1 + (d2/td)*model2)

    else:
        if d1 <= a:
            model1 = (3*d1/(4*a)) - 0.125*(d1/a)**3
        else:
            model1 = 1 - (3*a/(8*d1))

        if d2 <= a:
            model2 = (3*d2/(4*a)) - 0.125*(d2/a)**3
        else:
            model2 = 1 - (3*a/(8*d2))

        return C0 + C * ((d1/td)*model1 + (d2/td)*model2)

# Computation of 𝛾ҧ(𝐴𝐵, 𝐺) with Linear Model:
def linear_model(C0, C, d1, d2):
    if C != 1:
        if d1 > 0:
            model1 = d1 / 2
        else:
            model1 = 0

        if d2 > 0:
            model2 = d2 / 2
        else:
            model2 = 0

        return C0 + C * (model1 + model2)

    else:
        if d1 > 0:
            model1 = d1
        else:
            model1 = 0

        if d2 > 0:
            model2 = d2
        else:
            model2 = 0

        return C0

# Computation of 𝛾ҧ(𝐴𝐵, 𝐴𝐵) with Spherical Model::
def auxiliary_function_f(C0, C, a, td):
    if td <= a:
        return C0 + C * (td/(2*a) - (td**3)/(20*(a**3)))

    else:
        return C0 + C * (1 - (3*a/(4*td)) + (a**2)/(5*(td**2)))

# Computation of 𝛾ҧ(𝐴𝐵, 𝐴𝐵) with Linear Model:
def auxiliary_function_f_linear_model(C0, C, td):
    if td > 0:
        return C0 + C * (td/3)

    else:
        return C0

# A 95% confidence interval for the true mean thickness:
def probability_distribution_function(sigma, thickness):
    lower_bound = thickness - 1.96*sigma
    upper_bound = thickness + 1.96*sigma

    if upper_bound < 0:
        raise ValueError("The upper bound of variance can not be negative! Please try different model.")

    if lower_bound <= 0:
        lower_bound == 0

    return f'({lower_bound:.2f} < Z < {upper_bound:.2f}) = 0.95'

if model == "spherical_model":
    sigma1 = spherical_model(Sill, Nugget, Range, distance1, distance2, total_distance)
    sigma2 = auxiliary_function_f(Nugget, Sill, Range, total_distance)

elif model == "linear_model":
    sigma1 = linear_model(Nugget, Sill, distance1, distance2)
    sigma2 = auxiliary_function_f_linear_model(Nugget, Sill, total_distance)

sigma = (2*sigma1 - sigma2)**0.5

print("The true mean thickness of G:", probability_distribution_function(sigma, thicknessOfG))
