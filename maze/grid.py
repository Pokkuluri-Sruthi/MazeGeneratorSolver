from maze.cell import Cell


class Grid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = []

        for row in range(rows):
            current_row = []

            for col in range(cols):
                current_row.append(Cell(row, col))

            self.cells.append(current_row)

        # Start and end
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]

        return None

    def get_neighbors(self, row, col):
        neighbors = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append(self.cells[nr][nc])

        return neighbors

    def get_open_neighbors(self, row, col):
        cell = self.get_cell(row, col)

        if cell is None:
            return []

        neighbors = []

        # Top
        if not cell.walls["top"] and row > 0:
            neighbors.append(self.cells[row - 1][col])

        # Right
        if not cell.walls["right"] and col < self.cols - 1:
            neighbors.append(self.cells[row][col + 1])

        # Bottom
        if not cell.walls["bottom"] and row < self.rows - 1:
            neighbors.append(self.cells[row + 1][col])

        # Left
        if not cell.walls["left"] and col > 0:
            neighbors.append(self.cells[row][col - 1])

        return neighbors

    def reset(self):
        self.cells = []

        for row in range(self.rows):
            current_row = []

            for col in range(self.cols):
                current_row.append(Cell(row, col))

            self.cells.append(current_row)

    def get_grid(self):
        return self.cells