# Useful tools that can be used ANYTIME.
import random
import math
import matplotlib.pyplot as plt
import numpy as np


def list_of_consecutive_nums(mini, maxi):
    """
    :param maxi: maximum number of list
    :param mini: minimum number of list
    :return: the list of all consecutive numbers, shuffled.
    """
    ls = list(range(mini, maxi))
    return ls


def create_cubes(n):
    """
    :param n: the max number n
    :return: yield the value of x cubed.
    NOTE: If you are going to use this, make sure to ITERATE through function.
    """
    for x in range(n):
        yield x ** 3


def gen_fibo(n):
    """
    :param n: the max number of how many times fibonacci should return
    :return: yield fibonacci value 'a'.
    NOTE: If you are going to use this, make sure to ITERATE through function.
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


class Circle:
    """
    This is a class Circle where MOST properties of a circle is.
    """
    pi = 3.14

    def __init__(self, radius=1):
        """
        :param radius: Must be an int; area is pre-defined here for later use.
        """
        self.radius = radius
        self.area = radius ** 2 * Circle.pi

    def circumference(self):
        """
        :return: c, where c = 2*R*pi
        """
        return self.radius * 2 * Circle.pi


class Line:
    """
    This is a class Line where MOST properties of a Line is.
    """

    def __init__(self, coor1, coor2):  # expecting tuples. (9,10) (8,7)
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # distance = square root of (x2-x1)squared + (y2-y1))squared
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        # slope = y2 - y1 / x2 - x1
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        # volume = pi * r**2 * h
        return Cylinder.pi * self.radius ** 2 * self.height

    def surface_area(self):
        # surface area =  2(2pir^2) + (2pir^2 * H)
        return (2 * Cylinder.pi * self.radius ** 2) + (2 * Cylinder.pi * self.radius * self.height)
        pass


"""
NOTE: When using these functions, note that you can change the equation anytime,
but it must be related to the function itself. The functions return the range.
You can pair these functions with a graph module.
"""

def linear(x, m=1, b=1):
    return (m * x) + b

def quadratic(x, a=1, b=1, c=1):
    return a * (x ** 2) + b * x + c

def cubic(x):
    return x ** 3

def radical(x):
    return math.sqrt(x)

def logarithmic(x):
    return math.log10(x)

def exponential(x):
    return math.e ** x

def trigonometric_sine(x):
    return math.sin(x)

def trigonometric_cosine(x):
    return math.cos(x)

def trigonometric_tangent(x):
    """
    :param x: a number
    :return: tangent of x
    NOTE: When using this specific function, make sure to make x as increments of π, or the asymptotes.
    """
    return np.tan(x)

def absolute(x):
    return abs(x)

def rational(x, a=1, h=0, k=0):
    return (a / x - h) + k

# def polynomial(x):
#     return 2*x**3 - 3*x**2 + 4*x - 5


def even_check(num):
    return num % 2 == 0


def sqr(num):
    """
    :param num:
    :return:
    NOTE: If you have to apply to a list of numbers, use list(map(function, list)).
    """
    return num ** 2


def graph(x, y):
    """
    :param x: expecting a list of domains
    :param y: expecting a list of ranges
    :return: null. Only showing a graph.
    """
    fig, ax = plt.subplots()
    # Set the x and y limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    # Add a title and labels
    ax.set_title('Four Quadrant Chart')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    # Draw the quadrant lines
    ax.plot([-10, 10], [0, 0], 'k-')
    ax.plot([0, 0], [-10, 10], 'k-')
    plt.plot(x,y)
    print("Displaying Graph...")
    plt.show()


def percent_change(o=1,n=1):
    sym = ""
    if o > n:
        change = o-n
        sym = "-"
    elif n > o:
        change = n-o
        sym = "+"
    else:
        return 0

    return sym + str((change*100) / o)


if __name__ == '__main__':
    """
    to use functions: 
    x = list_of_consecutive_nums(1, 20)
    y = [0] * len(x)
    count = 0
    for n in x:
        y[count] = f(n)
        count += 1

    print(x)
    print(y)
    graph(x, y)
    """
