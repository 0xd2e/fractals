#!/usr/bin/python3

"""FRACTALS: LINDENMAYER SYSTEM"""


import numpy as np
import matplotlib.pyplot as plt


PRECISION = np.float32


def calc_rot_matrix(angle):
    """
    Input:

    angle
    -- integer or float number
    -- rotation angle in radians
    -- positive number gives counter-clockwise direction of rotation (turns left)
    -- negative number gives clockwise direction of rotation (turns right)


    Returns 2x2 numpy array of floats, a 2D rotation matrix.
    """

    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]], dtype=PRECISION)


def generate_pattern(lvl, states, rewrite_rules):
    """
    Inputs:

    lvl
    -- integer number
    -- the number of times (iterations) rewrite rules will be applied

    states -- string, the initial state (axiom) of the system

    rewrite_rules
    -- dictionary
    -- keys (character) -> symbols
    -- values (string) -> replacement rules


    Returns string of symbols.
    """

    # In each iteration: check every character in states, replace valid symbol
    # with rewrite rule or copy character, and update states
    for _ in range(lvl + 1):
        states = ''.join([rewrite_rules.get(symbol, symbol) for symbol in states])

    # Clean states form rewrite rule flags/symbols
    drawing_rules = 'F+-'
    states = ''.join([symbol for symbol in states if symbol in drawing_rules])

    return states


def generate_points(alpha, theta, length, states):
    """
    Inputs:

    alpha
    -- integer or float number
    -- angle (in degrees) between the positive x axis
       and initial displacement vector

    theta
    -- integer or float number
    -- angle (in degrees) of a single rotation

    length
    -- integer or float number
    -- length of a displacement vector for one step

    states -- string of symbols


    Retrurns numpy array of coordinates of points on a plane.


    Notes:

    ** Initial displacement vector starting point is allways
       in the origin of the coordinate system.

    ** Only character F in states (alphabet) generates a new point.
    """

    # Convert angles from degrees to radians
    alpha = np.radians(alpha)
    theta = np.radians(theta)

    # Displacement vector, 2x1 numpy array
    vec = np.array([[np.cos(alpha)], [np.sin(alpha)]], dtype=PRECISION)
    vec_len = np.sqrt(vec[0] ** 2 + vec[1] ** 2)

    # Rescale displacement vector
    vec = vec / vec_len * length

    # Rotation matrices for positive and negative angles
    rot_left = calc_rot_matrix(theta)
    rot_right = calc_rot_matrix(-theta)

    # Container to store xy components/coordinates of points on a plane
    points = np.zeros(shape=(2, states.count('F') + 1), dtype=PRECISION)

    point_index = 1

    for st in states:
        if st == '+':
            vec = np.dot(rot_right, vec)
        elif st == '-':
            vec = np.dot(rot_left, vec)
        else:
            points[:, point_index] = points[:, point_index - 1] + vec[:, 0]
            point_index += 1

    return points


def lindemayer(lvl, length, init_angle, angle, init_state,
               title='LINDENMAYER FRACTAL', color='#0080FF', **rewrite_rules):
    """
    Inputs:

    lvl
    -- integer number
    -- the number of times (iterations) rewrite rules will be applied

    length
    -- integer or float number
    -- length of a displacement vector of each step

    init_angle
    -- integer or float number
    -- initial angle (in degrees) measured from the positive x axis

    angle
    -- integer or float number
    -- angle (in degrees) of a single rotation
    -- positive number gives counter-clockwise direction of rotation (turns left)
    -- negative number gives clockwise direction of rotation (turns right)

    init_state -- string, the initial state (axiom) of the system

    title -- string, title of the plot

    color -- string, valid matplotlib color

    rewrite_rules
    -- keyword arguments
    -- keys (character) hold flags/symbols
    -- values (string) hold rules for production/replacement


    Displays the plot of calculated sequence of points.


    This function does not return any value.
    """

    states = generate_pattern(lvl, init_state, rewrite_rules)
    points = generate_points(init_angle, angle, length, states)

    plt.ioff()

    plt.figure(num=title, facecolor='white', frameon=False, clear=True)

    plt.style.use('fivethirtyeight')
    plt.grid(False)
    plt.axis('off')
    plt.axis('equal')

    plot_options = {
        'color': color,
        'alpha': 0.5,
        'linestyle': '-',
        'linewidth': 1.3,
        'marker': '',
        'antialiased': False,
    }

    plt.plot(points[0, :], points[1, :], **plot_options)
    plt.show()


def heighway_dragon(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'FX', 'HEIGHWAY DRAGON',
               X='X+YF+', Y='-FX-Y')


def twin_dragon(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'FX+FX+', 'TWIN DRAGON',
               X='X+YF', Y='FX-Y')


def tetra_dragon(lvl, length=1, init_angle=0, angle=120):
    lindemayer(lvl, length, init_angle, angle, 'F', 'TETRA DRAGON',
               F='F+F-F')


def levy_dragon(lvl, length=1, init_angle=90, angle=45):
    lindemayer(lvl, length, init_angle, angle, 'F', 'LEVY DRAGON',
               F='+F--F+')


def koch_snowflake(lvl, length=1, init_angle=0, angle=60):
    lindemayer(lvl, length, init_angle, angle, 'F++F++F', 'KOCH SNOWFLAKE',
               F='F-F++F-F')


def koch_curve(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'F+F+F+F', 'KOCH CURVE',
               F='F+F-F-FF+F+F-F')


def sierpinski_triangle(lvl, length=1, init_angle=0, angle=120):
    lindemayer(lvl, length, init_angle, angle, 'F+F+F', 'SIERPINSKI TRIANGLE',
               F='F+F-F-F+F')


def hilbert_curve(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'X', 'HILBERT CURVE',
               X='-YF+XFX+FY-', Y='+XF-YFY-FX+')


def moor_curve(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'XFX+F+XFX', 'MOOR CURVE',
               X='-YF+XFX+FY-', Y='+XF-YFY-FX+')


def peano_curve(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'X', 'PEANO CURVE',
               X='XFYFX+F+YFXFY-F-XFYFX', Y='YFXFY-F-XFYFX+F+YFXFY')


def tiles(lvl, length=1, init_angle=0, angle=90):
    lindemayer(lvl, length, init_angle, angle, 'F+F+F+F', 'TILES',
               F='FF+F-F+F+FF')


def pentadendryt(lvl, length=2, init_angle=0, angle=72):
    lindemayer(lvl, length, init_angle, angle, 'F', 'PENTADENDRYT',
               F='F+F-F--F+F+F')


if __name__ == '__main__':
    heighway_dragon(7)
    # twin_dragon(10)
    # tetra_dragon(6)
    # levy_dragon(13)
    koch_snowflake(2)
    # koch_curve(2)
    # sierpinski_triangle(5)
    # hilbert_curve(5)
    moor_curve(4)
    # peano_curve(3)
    # tiles(2)
    # pentadendryt(4)
