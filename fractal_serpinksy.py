import matplotlib.pyplot as plt
import numpy as np


def draw_triangle(ax, vertex, colour):
    triangle = plt.Polygon(vertex, edgecolor='k', facecolor=colour)
    ax.add_patch(triangle)


def fractal_serpinsky(ax, vertex, depth):
    colour = 'white' if depth == 0 else 'black'
    draw_triangle(ax, vertex, colour)
    if depth > 0:
        vertex = np.array(vertex)
        mid01 = (vertex[0] + vertex[1]) / 2
        mid12 = (vertex[1] + vertex[2]) / 2
        mid20 = (vertex[2] + vertex[0]) / 2
        fractal_serpinsky(ax, [vertex[0], mid01, mid20], depth - 1)
        fractal_serpinsky(ax, [vertex[1], mid12, mid01], depth - 1)
        fractal_serpinsky(ax, [vertex[2], mid20, mid12], depth - 1)


def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    vertex = [[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]]
    depth = int(input("Fractal depth: "))
    fractal_serpinsky(ax, vertex, depth)
    plt.show()


if __name__ == "__main__":
    main()
