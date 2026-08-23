import streamlit as st


def header():

    st.title("🧩 Maze Generator & Solver")

    st.markdown(
        """
        Generate a random maze and visualize different
        pathfinding algorithms step-by-step.
        """
    )

    st.divider()