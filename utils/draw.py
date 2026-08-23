import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from utils.colors import (
    BACKGROUND,
    WALL,
    PATH,
    VISITED,
    START,
    END,
    CELL
)


def draw_maze(
    grid,
    path=None,
    visited=None
):

    rows = len(grid)
    cols = len(grid[0])

    path = path or []
    visited = visited or []

    path_set = set(path)
    visited_set = set(visited)

    fig, ax = plt.subplots(
        figsize=(10, 10)
    )

    ax.set_facecolor(BACKGROUND)

    for row in range(rows):

        for col in range(cols):

            x = col
            y = rows - row - 1

            position = (row, col)

            face_color = CELL

            if position in visited_set:
                face_color = VISITED

            if position in path_set:
                face_color = PATH

            if position == (0, 0):
                face_color = START

            if position == (rows - 1, cols - 1):
                face_color = END

            rectangle = Rectangle(
                (x, y),
                1,
                1,
                facecolor=face_color,
                edgecolor="none"
            )

            ax.add_patch(rectangle)

            cell = grid[row][col]

            # Top wall
            if cell.walls["top"]:
                ax.plot(
                    [x, x + 1],
                    [y + 1, y + 1],
                    color=WALL,
                    linewidth=2
                )

            # Right wall
            if cell.walls["right"]:
                ax.plot(
                    [x + 1, x + 1],
                    [y, y + 1],
                    color=WALL,
                    linewidth=2
                )

            # Bottom wall
            if cell.walls["bottom"]:
                ax.plot(
                    [x, x + 1],
                    [y, y],
                    color=WALL,
                    linewidth=2
                )

            # Left wall
            if cell.walls["left"]:
                ax.plot(
                    [x, x],
                    [y, y + 1],
                    color=WALL,
                    linewidth=2
                )

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)

    ax.set_aspect("equal")

    ax.axis("off")

    plt.tight_layout()

    return fig