from rest_framework import serializers

from orders.models import Order, Category
from orders.serializers.category import CategorySerializer


class OrderSerializer(serializers.Serializer):
    """
    Serialize each field manually
    """

    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)
    is_active = serializers.BooleanField()
    price = serializers.DecimalField(
        max_digits=7, decimal_places=2, coerce_to_string=False)
    category = serializers.CharField()

    def create(self, validated_data):
        category = self.prepare_category(validated_data["category"])
        return Order.objects.create(
            title=validated_data.get("title"),
            description=validated_data.get("description"),
            is_active=validated_data.get("is_active"),
            price=validated_data.get("price"),
            category=category,
        )

    def update(self, instance, validated_data):
        category = self.prepare_category(validated_data["category"])

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.is_active = validated_data.get(
            "is_active", instance.is_active)
        instance.price = validated_data.get("price", instance.price)
        instance.category = category
        return instance

    def prepare_category(self, name):
        return Category.objects.get_or_create(name=name)[0]


###### 21.11.2019 CZEGO SIĘ DZISIAJ NAUCZYŁEM ??? ####
# * metody create(self, validated_data) oraz update(self, instance, validated_data) do tworzenia / modyfikowania obiektu
# * atrybut `format` w DateTimeField
