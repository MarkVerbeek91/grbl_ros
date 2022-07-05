"""
    Dummy conftest.py for grbl_ros.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import sys
from pathlib import Path


def add_test_doubles():
    sys.path.append(str(Path(__file__).parent / "test_doubles"))


add_test_doubles()

print(sys.path)
