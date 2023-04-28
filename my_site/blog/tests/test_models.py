import pytest
from .factories import TagFactory

pytestmark = pytest.mark.django_db


def test_str_method(tag_factory):
    # Arrange
    tag = TagFactory(caption="Test tag")
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
