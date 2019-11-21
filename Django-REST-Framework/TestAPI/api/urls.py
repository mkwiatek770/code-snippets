from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from users import views as user_views
from orders import views as order_views

router = routers.DefaultRouter()
router.register('users', user_views.UserViewSet)
router.register('groups', user_views.GroupViewSet)
router.register('orders', order_views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),  # login / logout
]
