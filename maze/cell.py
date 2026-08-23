class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Walls: top, right, bottom, left
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

        self.visited = False

    def remove_wall(self, other):
        row_difference = other.row - self.row
        col_difference = other.col - self.col

        # Other cell is below
        if row_difference == 1:
            self.walls["bottom"] = False
            other.walls["top"] = False

        # Other cell is above
        elif row_difference == -1:
            self.walls["top"] = False
            other.walls["bottom"] = False

        # Other cell is right
        elif col_difference == 1:
            self.walls["right"] = False
            other.walls["left"] = False

        # Other cell is left
        elif col_difference == -1:
            self.walls["left"] = False
            other.walls["right"] = False

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"