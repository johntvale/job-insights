import pytest
from src.counter import count_ocurrences


def test_counter():
    VALID_PY = 1639
    VALID_JS = 122

    assert count_ocurrences('src/jobs.csv', 'Python') == VALID_PY
    assert count_ocurrences('src/jobs.csv', 'Javascript') == VALID_JS

    with pytest.raises(TypeError):
        count_ocurrences('src/jobs.csv')
        count_ocurrences()

    with pytest.raises(AssertionError):
        assert count_ocurrences('src/jobs.csv', 'Python') != VALID_PY
        assert count_ocurrences('src/jobs.csv', 'Javascript') != VALID_JS
