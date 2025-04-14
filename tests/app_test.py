import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md

def test_info():
    at = AppTest.from_file("app.py").run()

    # we start from -3 because for some reason the sidebar's copyright
    # text is set as last in list even if called first.
    assert at.markdown[-3].body.strip() == addr_md.strip()
    assert at.markdown[-2].body.strip() == links_md.strip()

def test_login():
    at = AppTest.from_file("app.py").run()

    at.session_state.logged_in = False

    at.button("login").click().run()

    assert at.session_state.logged_in == True

    at.button("logout").click().run()

    assert at.session_state.logged_in == False
