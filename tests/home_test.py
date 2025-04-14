import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


def test_home_page_markdown():
    at = AppTest.from_file("page/home.py").run()

    assert at.markdown[0].body == "# Welcome to Streamlit!"
    assert at.markdown[1].body.startswith("This website has a lot of redundant code.")
