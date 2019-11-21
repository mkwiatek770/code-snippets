from rest_framework import viewsets
from orders.models import Order
from orders.serializers.order import OrderSerializer

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-date_created')
