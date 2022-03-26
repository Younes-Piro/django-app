from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Books
from .models import Accessory


# @registry.register_document
# class BooksDocument(Document):
#     class Index:
#         name = 'books'

#     class Django:
#          model = Books
#          fields = [
#             'title'
#         ]
@registry.register_document
class AccessoriesDocument(Document):
    class Index:
        name = 'accessories'

    class Django:
         model = Accessory
         fields = [
            'title'
        ]