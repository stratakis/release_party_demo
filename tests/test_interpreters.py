import os
import pytest
from flexmock import flexmock

from release_party_demo.interpreters import get_py_interpreters


@pytest.mark.parametrize(('bin_dir', 'expected'), [
    (['python3.3', 'cmake', 'git'], ['python3.3']),
    (['python3.5', 'pypy3'], ['python3.5', 'pypy3']),
    ([], [])
])
def test_interpreters(bin_dir, expected):
    flexmock(os).should_receive('listdir').and_return(bin_dir)
    assert [i for i in get_py_interpreters()] == expected
