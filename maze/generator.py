import random


class MazeGenerator:

    def __init__(self, grid):
        self.grid = grid

        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_unvisited_neighbors(self, cell):
        neighbors = []

        row = cell.row
        col = cell.col

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

                neighbor = self.grid[nr][nc]

                if not neighbor.visited:
                    neighbors.append(neighbor)

        return neighbors

    def generate(self):
        # Start from top-left
        current = self.grid[0][0]
        current.visited = True

        stack = [current]

        while stack:

            current = stack[-1]

            neighbors = self.get_unvisited_neighbors(current)

            if neighbors:

                next_cell = random.choice(neighbors)

                current.remove_wall(next_cell)

                next_cell.visited = True

                stack.append(next_cell)

            else:
                stack.pop()

        # Reset visited status after generation
        for row in self.grid:
            for cell in row:
                cell.visited = False

        return self.grid