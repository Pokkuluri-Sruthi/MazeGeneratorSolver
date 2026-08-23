import heapq


class Dijkstra:

    def __init__(self, grid):
        self.grid = grid
        self.visited = []
        self.path = []

    def solve(self, start, end):

        distances = {
            start: 0
        }

        parent = {
            start: None
        }

        heap = [
            (0, start)
        ]

        visited_set = set()

        while heap:

            distance, current = heapq.heappop(heap)

            if current in visited_set:
                continue

            visited_set.add(current)

            self.visited.append(current)

            if current == end:
                break

            row, col = current

            neighbors = self.grid.get_open_neighbors(row, col)

            for neighbor in neighbors:

                position = (neighbor.row, neighbor.col)

                new_distance = distance + 1

                if new_distance < distances.get(position, float("inf")):

                    distances[position] = new_distance

                    parent[position] = current

                    heapq.heappush(
                        heap,
                        (new_distance, position)
                    )

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