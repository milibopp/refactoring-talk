from math import sqrt, acos, pi

def theta(a, b):
    if len(a) == 2:
        # Calculate the length of both 2D vectors
        len_a = sqrt(a[0] ** 2 + a[1] ** 2)
        length_b = sqrt(b[0] ** 2 + b[1] ** 2)
        # Calculate the dot product of 2D vectors
        ab = a[0] * b[0] + a[1] * b[1]
        # Get result from formula and convert to degrees
        return acos(ab / (len_a * length_b)) / pi * 180
    elif len(a) == 3:
        # Calculate the length of both 3D vectors
        la = sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
        lb = sqrt(b[0] ** 2 + b[1] ** 2 + a[2] ** 2)
        # Calculate the dot product of 3D vectors
        dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
        # Get result from formula and convert to degrees
        return acos(dot / (la * lb)) / pi * 180
