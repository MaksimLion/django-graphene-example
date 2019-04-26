import graphene

import example.schema


class Query(example.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)