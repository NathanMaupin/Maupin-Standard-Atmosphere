# Outputs Temp (R), Pressure (lb/ft^2), Density (slugs/ft^3), Speed of sound (ft/s)
from math import e

r = 20925000  # radius of Earth
g = 32.2  # Earth's gravity in ft/s^2
R = 1716  # R Constant in lb/R
a_list = [-0.00357, 0, 0.00165, 0, -0.00247]
alt = [0, 36089.2, 82021, 154199, 173885, 259186]
temp_list = [518.69, 389.09, 508.79]
ps = 2116.2
ds = 0.002377


def calculator(a, t0, h0, h1):  # Function for general formulas for a, Temp, Pressure, Density, and Speed of Sound

    grad_step = 0  # Iterating through lists
    p0 = ps
    d0 = ds
    t0_mod = temp_list[0]  # base value for initial temp
    h0point = alt[grad_step]  # range of altitudes
    h1point = alt[grad_step + 1]

    if h1 < alt[grad_step + 1]:  # Calculating temp if within first gradient
        t = t0 + a * (h1 - h0)
    while h1 > alt[grad_step + 1]:  # If inputted height greater than upper constraint of gradient/isothermal region

        t = t0_mod + a_list[grad_step] * (
                    h1point - h0point)  # Calculating temp for either gradient or isothermal region

        if a_list[grad_step] != 0:  # Checks if region is a gradient or isothermal
            p = p0 * (t / t0_mod) ** (-g / a_list[grad_step] / R)
            d = d0 * (t / t0_mod) ** ((-g / a_list[grad_step] / R) + 1)
        else:  # If the region is isothermal
            p = p0 * e ** ((-1 * (g / R / t)) * (h1point - h0point))
            d = d0 * e ** ((-1 * (g / R / t)) * (h1point - h0point))

        t0_mod = t
        p0 = p
        d0 = d
        if h1 > alt[grad_step + 1]:  # Continues to iterate if loop is still valid
            grad_step = grad_step + 1

    if a_list[grad_step] != 0:  # Checks final region if it's a gradient
        h0point = alt[grad_step]
        h1point = h1
        t_1 = t0_mod + a_list[grad_step] * (h1point - h0point)
        p = p0 * (t_1 / t0_mod) ** (-g / a_list[grad_step] / R)
        d = d0 * (t / t0_mod) ** ((-g / a_list[grad_step] / R) + 1)
    else:  # If final region is isothermal
        h0point = alt[grad_step]
        h1point = h1
        p = p0 * e ** ((-1) * ((g / R / t) * (h1 - h0)))
        d = d0 * e ** ((-1 * (g / R / t)) * (h1point - h0point))

    # Final Outputs of a given altitude
    print("Temperature: ", t, "R")
    print("Pressure: ", p, " lb/ft^2")
    print("Density: ", d, " slugs/ft^3")


# User inputs a Geometric Altitude
print("Enter an Geometric Altitude in feet: ")
hg = int(input())
h = (r / (r + hg)) * hg  # Geometric Altitude converted to Geopotential Altitude

count = 0
match = True
while match:  # Sets initial constraints for calling function
    if alt[count] <= h < alt[count + 1]:
        calculator(a_list[count], temp_list[count], alt[count], h)
        match = False  # Breaks loop if conditions met
    count = count + 1