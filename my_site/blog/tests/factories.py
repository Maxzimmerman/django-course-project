from ..models import Tag, Author, Post, Comment
import factory


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("word", max_nb_chars=10)
