from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Books

@registry.register_document
class BooksDocument(Document):
    class Index:
        name = 'books'

    class Django:
         model = Books
         fields = [
            'title'
        ]