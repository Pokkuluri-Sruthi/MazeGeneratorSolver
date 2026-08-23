import streamlit as st

from components.header import header
from components.sidebar import sidebar
from components.stats import show_stats

from maze.grid import Grid
from maze.generator import MazeGenerator

from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar

from utils.draw import draw_maze


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Maze Generator & Solver",
    page_icon="🧩",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

header()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

(
    rows,
    cols,
    algorithm,
    speed,
    generate,
    solve,
    reset
) = sidebar()


# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

if "grid" not in st.session_state:

    st.session_state.grid = Grid(
        rows,
        cols
    )

    generator = MazeGenerator(
        st.session_state.grid.get_grid()
    )

    generator.generate()

    st.session_state.path = []
    st.session_state.visited = []
    st.session_state.algorithm = algorithm


# --------------------------------------------------
# RESET
# --------------------------------------------------

if reset:

    st.session_state.grid = Grid(
        rows,
        cols
    )

    generator = MazeGenerator(
        st.session_state.grid.get_grid()
    )

    generator.generate()

    st.session_state.path = []
    st.session_state.visited = []

    st.rerun()


# --------------------------------------------------
# GENERATE MAZE
# --------------------------------------------------

if generate:

    st.session_state.grid = Grid(
        rows,
        cols
    )

    generator = MazeGenerator(
        st.session_state.grid.get_grid()
    )

    generator.generate()

    st.session_state.path = []
    st.session_state.visited = []

    st.rerun()


# --------------------------------------------------
# HANDLE SIZE CHANGE
# --------------------------------------------------

current_grid = st.session_state.grid

if (
    current_grid.rows != rows
    or current_grid.cols != cols
):

    st.session_state.grid = Grid(
        rows,
        cols
    )

    generator = MazeGenerator(
        st.session_state.grid.get_grid()
    )

    generator.generate()

    st.session_state.path = []
    st.session_state.visited = []


# --------------------------------------------------
# SOLVE MAZE
# --------------------------------------------------

if solve:

    grid = st.session_state.grid

    start = grid.start
    end = grid.end

    if algorithm == "BFS":

        solver = BFS(grid)

    elif algorithm == "DFS":

        solver = DFS(grid)

    elif algorithm == "Dijkstra":

        solver = Dijkstra(grid)

    else:

        solver = AStar(grid)

    path, visited = solver.solve(
        start,
        end
    )

    st.session_state.path = path
    st.session_state.visited = visited
    st.session_state.algorithm = algorithm


# --------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------

left, right = st.columns(
    [3, 1]
)


# --------------------------------------------------
# MAZE DISPLAY
# --------------------------------------------------

with left:

    st.subheader("🗺️ Maze")

    figure = draw_maze(
        st.session_state.grid.get_grid(),
        st.session_state.path,
        st.session_state.visited
    )

    st.pyplot(
        figure,
        use_container_width=True
    )


# --------------------------------------------------
# INFORMATION PANEL
# --------------------------------------------------

with right:

    st.subheader("📌 Information")

    st.write(
        "**Start:** 🟢 Top-left"
    )

    st.write(
        "**End:** 🔴 Bottom-right"
    )

    st.write(
        f"**Maze Size:** {rows} × {cols}"
    )

    st.write(
        f"**Algorithm:** {algorithm}"
    )

    st.write(
        f"**Speed:** {speed}"
    )

    st.divider()

    visited_count = len(
        st.session_state.visited
    )

    path_length = len(
        st.session_state.path
    )

    show_stats(
        algorithm,
        visited_count,
        path_length
    )


# --------------------------------------------------
# LEGEND
# --------------------------------------------------

st.divider()

st.subheader("🎨 Legend")

legend1, legend2, legend3, legend4 = st.columns(4)

with legend1:
    st.write("🟢 Start")

with legend2:
    st.write("🔴 End")

with legend3:
    st.write("🟦 Visited")

with legend4:
    st.write("🟨 Path")


# --------------------------------------------------
# ALGORITHM DESCRIPTION
# --------------------------------------------------

st.divider()

st.subheader("🧠 Selected Algorithm")

descriptions = {

    "BFS":
        """
        **Breadth First Search** explores the maze level by level.
        In an unweighted maze, BFS guarantees the shortest path.
        """,

    "DFS":
        """
        **Depth First Search** explores one direction as deeply as
        possible before backtracking. It does not always produce
        the shortest path.
        """,

    "Dijkstra":
        """
        **Dijkstra's Algorithm** calculates the shortest distance
        from the starting cell to every reachable cell.
        """,

    "A*":
        """
        **A*** combines the distance already travelled with a
        heuristic estimate of the remaining distance.
        """
}

st.info(
    descriptions[algorithm]
)