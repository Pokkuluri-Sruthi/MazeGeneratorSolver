from collections import deque


class BFS:

    def __init__(self, grid):
        self.grid = grid
        self.visited = []
        self.path = []

    def solve(self, start, end):

        queue = deque([start])

        parent = {
            start: None
        }

        visited_set = {
            start
        }

        while queue:

            current = queue.popleft()

            self.visited.append(current)

            if current == end:
                break

            row, col = current

            neighbors = self.grid.get_open_neighbors(row, col)

            for neighbor in neighbors:

                position = (neighbor.row, neighbor.col)

                if position not in visited_set:

                    visited_set.add(position)

                    parent[position] = current

                    queue.append(position)

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