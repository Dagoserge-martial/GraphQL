import graphene
import compagnie.schema

class Query(compagnie.schema.Query, graphene.ObjectType):
    pass

class Mutation(compagnie.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)