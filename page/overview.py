import streamlit as st

st.markdown("# Overview")
st.sidebar.header("Overview")

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)