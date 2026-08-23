import streamlit as st


def sidebar():

    st.sidebar.header("⚙️ Maze Settings")

    rows = st.sidebar.slider(
        "Rows",
        min_value=5,
        max_value=40,
        value=15
    )

    cols = st.sidebar.slider(
        "Columns",
        min_value=5,
        max_value=40,
        value=15
    )

    algorithm = st.sidebar.selectbox(
        "Pathfinding Algorithm",
        [
            "BFS",
            "DFS",
            "Dijkstra",
            "A*"
        ]
    )

    speed = st.sidebar.slider(
        "Animation Speed",
        min_value=1,
        max_value=10,
        value=5
    )

    st.sidebar.divider()

    generate = st.sidebar.button(
        "🎲 Generate Maze",
        use_container_width=True
    )

    solve = st.sidebar.button(
        "🚀 Solve Maze",
        use_container_width=True
    )

    reset = st.sidebar.button(
        "🔄 Reset",
        use_container_width=True
    )

    return (
        rows,
        cols,
        algorithm,
        speed,
        generate,
        solve,
        reset
    )