from rest_framework import serializers
from orders.models import Category


class CategorySerializer(serializers.Serializer):

    category = serializers.ChoiceField(Category.objects.all())
