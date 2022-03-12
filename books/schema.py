import graphene
from .models import Books, Accessory
from .mutation import BooksCreateMutation, BooksType, BooksUpdateMutation, BooksDeleteMutation, AccessoryType

# query are useful to query the data from our database

class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType)
    single_book = graphene.Field(BooksType, id=graphene.Int()) #getting a single book my id
    all_accessories = graphene.List(AccessoryType)

    def resolve_all_books(root, info):
        return Books.objects.all()
        
    def resolve_single_book(root, info, id):
        return Books.objects.get(pk=id)
    
    def resolve_all_accessories(root, info):
        return Accessory.objects.all()

# mutation class to modify data from our database
class Mutation(graphene.ObjectType):
    create_book = BooksCreateMutation.Field()
    update_book = BooksUpdateMutation.Field()
    delete_book = BooksDeleteMutation.Field()


    



# importing the schema
schema = graphene.Schema(query=Query , mutation=Mutation)