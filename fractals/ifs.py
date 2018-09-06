#!/usr/bin/python3

"""FRACTALS: ITERATED FUNCTION SYSTEM"""


import numpy as np
import matplotlib.pyplot as plt

from numba import jit


PRECISION = np.float32


def plotf(x, y, win_title='ITERATED FUNCTION SYSTEM FRACTAL', color='#0080FF'):
    """
    Inputs:

    x, y
    -- tuple, list, or numpy array of numbers
    -- must have the same length
    -- coordinates of points on a plane

    win_title
    -- string, title of the plot window
    -- default: ITERATED FUNCTION SYSTEM FRACTAL

    color
    -- string, valid matplotlib color
    -- default: #0080FF


    Displays the scatter plot of the given points.


    This function does not return any value.
    """

    plt.ioff()

    plt.figure(num=win_title, facecolor='white', frameon=False, clear=True)

    plt.style.use('fivethirtyeight')
    plt.grid(False)
    plt.axis('off')
    plt.axis('equal')

    plot_options = {
        'color': color,
        'alpha': 0.5,
        'linestyle': '',
        'marker': 'o',
        'markersize': 1,
        'markeredgewidth': 0,
        'markeredgecolor': '#CC2EFA',
        'markerfacecolor': '#00BFFF'
    }

    plt.plot(x, y, **plot_options)
    plt.show()


@jit(nopython=True)
def ifs(lvl, p, a, b, c, d, e, f):
    """
    Inputs:

    lvl -- integer, number of iterations

    p, a, b, c, d, e, f
    -- tuple, list, or numpy array of numbers
    -- IFS parameters
    -- all must have the same length
    -- p must be sorted in descending order and other
       parameters must be adjusted accordingly


    Return a tuple with two 1D numpy arrays, each of size lvl + 1,
    with calculated xy coordinates.
    """

    lvl += 1
    param_indexes = range(len(p))

    # Containers to store xy components/coordinates of points on a plane
    x = np.zeros(shape=lvl, dtype=PRECISION)
    y = np.zeros(shape=lvl, dtype=PRECISION)

    for i in range(1, lvl):

        temp = np.random.random()

        # i -- index for containers
        # j -- index for parameters

        for j in param_indexes:

            if temp > p[j]:
                x[i] = a[j] * x[i - 1] + b[j] * y[i - 1] + e[j]
                y[i] = c[j] * x[i - 1] + d[j] * y[i - 1] + f[j]
                break

    return x, y


def spiral(lvl):
    p = (0.104348, 0.052174, -1.0)
    a = (0.787879, -0.121212, 0.181818)
    b = (-0.424242, 0.257576, -0.136364)
    c = (0.242424, 0.151515, 0.090909)
    d = (0.859848, 0.053030, 0.181818)
    e = (1.758647, -6.721654, 6.086107)
    f = (1.408065, 1.377236, 1.568035)
    x, y = ifs(lvl, p, a, b, c, d, e, f)
    plotf(x, y, 'IFS SPIRAL')


def dragon(lvl):
    p = (0.212527, -1.0)
    a = (0.824074, 0.088272)
    b = (0.281428, 0.520988)
    c = (-0.212346, -0.463889)
    d = (0.864198, -0.377778)
    e = (-1.882290, 0.785360)
    f = (-0.110607, 8.095795)
    x, y = ifs(lvl, p, a, b, c, d, e, f)
    plotf(x, y, 'IFS DRAGON')


def fern_leaf(lvl):
    p = (0.15, 0.08, 0.01, -1.0)
    a = (0.85, -0.15, 0.20, 0.0)
    b = (0.04, 0.28, -0.26, 0.0)
    c = (-0.04, 0.26, 0.23, 0.0)
    d = (0.85, 0.24, 0.22, 0.16)
    e = (0.0, 0.0, 0.0, 0.0)
    f = (1.6, 0.44, 1.6, 0.0)
    x, y = ifs(lvl, p, a, b, c, d, e, f)
    plotf(x, y, 'IFS FERN LEAF')


def maple_leaf(lvl):
    p = (0.65, 0.3, 0.1, -1.0)
    a = (0.43, 0.45, 0.49, 0.14)
    b = (0.52, -0.49, 0.0, 0.01)
    c = (-0.45, 0.47, 0.0, 0.0)
    d = (0.5, 0.47, 0.51, 0.51)
    e = (1.49, -1.62, 0.02, -0.08)
    f = (-0.75, -0.74, 1.62, -1.31)
    x, y = ifs(lvl, p, a, b, c, d, e, f)
    plotf(x, y, 'IFS MAPLE LEAF')


def sierpinski_triangle(lvl):
    p = (0.6666, 0.3333, -1)
    a = (0.5, 0.5, 0.5)
    b = (0.0, 0.0, 0.0)
    c = (0.0, 0.0, 0.0)
    d = (0.5, 0.5, 0.5)
    e = (0.5, -0.5, -0.5)
    f = (-0.5, 0.5, -0.5)
    x, y = ifs(lvl, p, a, b, c, d, e, f)
    plotf(x, y, 'IFS SIERPINSKI TRIANGLE')


@jit(nopython=True)
def clifford_attractor(lvl, a, b, c, d):
    """
    Inputs:

    lvl -- integer, number of iterations

    a, b, c, d -- numeric parameters


    Return a tuple with two 1D numpy arrays, each of size lvl + 1,
    with calculated xy coordinates.
    """

    lvl += 1

    # Containers to store xy components/coordinates of points on a plane
    x = np.zeros(shape=lvl, dtype=PRECISION)
    y = np.zeros(shape=lvl, dtype=PRECISION)

    for i in range(1, lvl):
        x[i] = np.sin(a * y[i - 1]) + c * np.cos(a * x[i - 1])
        y[i] = np.sin(b * x[i - 1]) + d * np.cos(b * y[i - 1])

    return x, y


if __name__ == '__main__':
    # spiral(90000)
    # dragon(90000)
    fern_leaf(60000)
    # maple_leaf(90000)
    # sierpinski_triangle(90000)
    # plotf(*clifford_attractor(100000, 1.5, -1.8, 1.6, 0.9), 'CLIFFORD ATTRACTOR', '#045FB4')
    plotf(*clifford_attractor(90000, 1.7, 1.7, 0.06, 1.2), 'CLIFFORD ATTRACTOR', '#045FB4')
    # plotf(*clifford_attractor(100000, -1.4, 1.6, 1.0, 0.7), 'CLIFFORD ATTRACTOR', '#045FB4')
