class DFS:

    def __init__(self, grid):
        self.grid = grid
        self.visited = []
        self.path = []

    def solve(self, start, end):

        stack = [start]

        parent = {
            start: None
        }

        visited_set = {
            start
        }

        while stack:

            current = stack.pop()

            self.visited.append(current)

            if current == end:
                break

            row, col = current

            neighbors = self.grid.get_open_neighbors(row, col)

            for neighbor in reversed(neighbors):

                position = (neighbor.row, neighbor.col)

                if position not in visited_set:

                    visited_set.add(position)

                    parent[position] = current

                    stack.append(position)

        self.path = self.build_path(parent, start, end)

        return self.path, self.visited

    def build_path(self, parent, start, end):

        if end not in parent:
            return []

        path = []

        current = end

        while current is not None:

            path.append(current)

            current = parent[current]

        path.reverse()

        return path