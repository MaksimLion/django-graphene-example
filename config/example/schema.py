import graphene

from graphene_django.types import DjangoObjectType
from .models import Category, Item


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query():
   
    all_categories = graphene.List(CategoryType)
    all_items = graphene.List(ItemType)

    item = graphene.Field(ItemType, id=graphene.Int(), name=graphene.String())
    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_items(self, info, **kwargs):
        return Item.objects.select_related('category').all()

    def resolve_item(self, info, **kwargs):
        item_id = kwargs.get('id')
        item_name = kwargs.get('name')

        if item_id is not None:
            return Item.objects.get(pk=item_id)

        if item_name is not None:
            return Item.objects.get(name=item_name)

        return None

    def resolve_category(self, info, **kwargs):
        category_id = kwargs.get('id')
        category_name = kwargs.get('name')

        if category_id is not None:
            return Category.objects.get(pk=category_id)

        if category_name is not None:
            return Category.objects.get(name=category_name)

        return None
