import streamlit as st


def show_stats(
    algorithm,
    visited_count,
    path_length
):

    st.subheader("📊 Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Algorithm",
            algorithm
        )

    with col2:
        st.metric(
            "Visited Cells",
            visited_count
        )

    with col3:
        st.metric(
            "Path Length",
            path_length
        )