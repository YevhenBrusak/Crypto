def find_points_on_curve(modulus=23):
    """
    Finds all points (x, y) that satisfy the elliptic curve equation:
    y^2 = (x^3 + x + 1) mod modulus

    Parameters:
        modulus (int): The modulus to use in the equation.

    Returns:
        list: A list of tuples representing the points (x, y) on the curve.
    """
    points = []  # List to store the valid points

    # Iterate over all possible values of x in the range [0, modulus - 1]
    for x in range(modulus):
        # Compute the right-hand side of the equation: (x^3 + x + 1) % modulus
        rhs = (x**3 + x + 1) % modulus

        # Iterate over all possible values of y in the range [0, modulus - 1]
        for y in range(modulus):
            # Compute the left-hand side of the equation: y^2 % modulus
            lhs = (y**2) % modulus

            # Check if lhs equals rhs (y^2 == x^3 + x + 1 mod modulus)
            if lhs == rhs:
                points.append((x, y))  # Add the valid point (x, y) to the list

    return points

def point_addition(P, Q, a, p):
    """
    Adds two points P and Q on the elliptic curve y^2 = x^3 + ax + b mod p.

    Parameters:
        P (tuple): The first point (x1, y1).
        Q (tuple): The second point (x2, y2).
        a (int): The coefficient of x in the curve equation.
        p (int): The modulus.

    Returns:
        tuple: The resulting point (x3, y3).
    """
    x1, y1 = P
    if P == Q:
        # Point doubling
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    else:
        # Point addition
        x2, y2 = Q
        if x1 == x2 and y1 != y2:
            return None  # P + (-P) = O
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m**2 - x1 - (x2 if P != Q else x1)) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3

def find_order_of_point(G, a, b, p):
    """
    Finds the order of a given point G on the elliptic curve y^2 = x^3 + ax + b mod p.

    Parameters:
        G (tuple): The base point (x, y).
        a (int): The coefficient of x in the curve equation.
        b (int): The constant term in the curve equation.
        p (int): The modulus.

    Returns:
        int: The order of the point G.
    """
    current_point = G
    for n in range(1, p + 1):
        if current_point is None:  # If we reach the identity element
            return n
        current_point = point_addition(current_point, G, a, p)
    return None  # If no order is found within the range

# Call the functions and print results
if __name__ == "__main__":
    curve_points = find_points_on_curve()
    print("Points on the elliptic curve y^2 = (x^3 + x + 1) mod 23:")
    print(", ".join([str(point) for point in curve_points]))

    # Testing the order of point G = (17, 25)
    G = (17, 25)
    a, b, p = 1, 1, 23  # Coefficients of the curve equation
    order = find_order_of_point(G, a, b, p)
    print(f"The order of the point {G} on the curve is: {order}")
