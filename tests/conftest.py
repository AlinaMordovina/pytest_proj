import pytest

words_dict = {"vcs": "mercurial", "upi": "upiter", "mrs": "mars"}


@pytest.fixture
def dict_fixture():
    return words_dict.copy()
