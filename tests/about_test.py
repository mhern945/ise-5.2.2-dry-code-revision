import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


def test_app_page_markdown():
    at = AppTest.from_file("page/about.py").run()

    assert at.markdown[0].body == "# About"
    assert at.markdown[1].body.startswith("Fake Company LLC Inc. is a fake company")
