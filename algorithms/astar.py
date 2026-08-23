import heapq


class AStar:

    def __init__(self, grid):
        self.grid = grid
        self.visited = []
        self.path = []

    def heuristic(self, current, end):

        r1, c1 = current
        r2, c2 = end

        return abs(r1 - r2) + abs(c1 - c2)

    def solve(self, start, end):

        g_score = {
            start: 0
        }

        f_score = {
            start: self.heuristic(start, end)
        }

        parent = {
            start: None
        }

        heap = [
            (f_score[start], start)
        ]

        visited_set = set()

        while heap:

            _, current = heapq.heappop(heap)

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

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(
                    position,
                    float("inf")
                ):

                    parent[position] = current

                    g_score[position] = tentative_g

                    f = tentative_g + self.heuristic(
                        position,
                        end
                    )

                    f_score[position] = f

                    heapq.heappush(
                        heap,
                        (f, position)
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