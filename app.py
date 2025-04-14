import streamlit as st

if st.session_state.get("logged_in") == None:
    st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


def sidebar():
    """Show log in/out info and copyright on sidebar"""
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")


def footer():
    """Show company info as dropdowns in footer"""
    with st.expander("Company Info"):
        st.write("Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043")

    with st.expander("Links"):
        st.markdown(
            """
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
        """
        )


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

home = st.Page("page/home.py", title="Home")
about = st.Page("page/about.py", title="About")
overview = st.Page("page/overview.py", title="Overview")
report = st.Page("page/report.py", title="Report")

pg = st.navigation([home, about, overview, report])
pg.run()

sidebar()
footer()
