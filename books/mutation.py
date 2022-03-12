import graphene
from .models import Books, Accessory
from graphene_django import DjangoListField, DjangoObjectType


class BooksType(DjangoObjectType): #serialisation the data from our model to graphql
    class Meta:
        model = Books
        fields = "__all__"

class AccessoryType(DjangoObjectType):
    class Meta:
        model = Accessory
        fields = "__all__"

class BooksCreateMutation(graphene.Mutation): #creating a schema for mutation
    class Arguments:
        title = graphene.String(required=True)

    book = graphene.Field(BooksType)

    @classmethod
    def mutate(cls, root, info, title):
        book = Books(title=title)
        book.save() #function in django
        return BooksCreateMutation(book=book)

#in graphql interface we use this schema 
'''
mutation bookmutation{
  createBook(title: "new title 3"){
    book{
      title
      id
    }
	}
}
'''        

class BooksUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
    
    book = graphene.Field(BooksType)

    @classmethod
    def mutate(cls, root, info, title, id):
        book = Books.objects.get(id=id)
        book.title = title
        book.save()
        return BooksUpdateMutation(book=book)


'''
mutation bookmutation{
  updateBook(title: "update title 3" , id: 11){
    book{
      title
      id
    }
	}
}
'''
class BooksDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    book = graphene.Field(BooksType)

    @classmethod
    def mutate(cls, root, info, id):
        book = Books.objects.get(id=id)
        book.delete()
        return BooksDeleteMutation(book=book)
