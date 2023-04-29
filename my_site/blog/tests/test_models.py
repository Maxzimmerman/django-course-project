import pytest
from my_site.blog.tests.factories import TagFactory


def test_str_method():
    # Arrange
    tag = TagFactory()
    # Act
    # Assert
    assert tag.__str__() == "Test tag"


class TestAuthor:
    pass


class TestPost:
    pass


class TestTag:
    pass


class TestComment:
    pass
