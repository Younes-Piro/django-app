from django_mongoengine import Document, EmbeddedDocument, fields

class Book(EmbeddedDocument):
    name = fields.StringField(max_length=255)
