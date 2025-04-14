import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


def test_app_page_markdown():
    at = AppTest.from_file("page/overview.py").run()

    assert at.markdown[0].body == "# Overview"
    assert at.markdown[1].body.startswith("Here is a page with a site overview.")
