import streamlit as st

st.markdown("# Report")
st.sidebar.header("Report")

st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
"""
)
