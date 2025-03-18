def equilateral(sides):
    """Check if a triangle is equilateral.

    :param sides: list or tuple of three side lengths.
    :return: bool - True if all sides are equal and greater than 0.
    """
    a, b, c = sides
    return a > 0 and a == b == c


def isosceles(sides):
    """Check if a triangle is isosceles.

    :param sides: list or tuple of three side lengths.
    :return: bool - True if at least two sides are equal and the triangle is valid.
    """
    a, b, c = sides
    return (a == b or a == c or b == c) and is_valid_triangle(sides)


def scalene(sides):
    """Check if a triangle is scalene.

    :param sides: list or tuple of three side lengths.
    :return: bool - True if all sides are different and the triangle is valid.
    """
    a, b, c = sides
    return a != b and b != c and a != c and is_valid_triangle(sides)


def is_valid_triangle(sides):
    """Check if the given sides form a valid triangle.

    :param sides: list or tuple of three side lengths.
    :return: bool - True if the sides satisfy the triangle inequality.
    """
    a, b, c = sorted(sides)
    return a > 0 and a + b > c