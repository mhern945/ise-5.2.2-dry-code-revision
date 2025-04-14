import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


@pytest.mark.timeout(10)  # Extra timeout because bar charts are slow
def test_app_page_markdown():
    at = AppTest.from_file("page/report.py").run()

    assert at.markdown[0].body == "# Report"
    assert at.markdown[1].body.startswith("Here is a page with a report on it.")
    assert at.markdown[2].body.strip() == ("Look at those numbers. Amazing.")
