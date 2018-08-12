from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from api.chat import views


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
router.register('users', views.UserViewSet)
rooms_router = router.register('rooms', views.RoomViewSet)
rooms_router.register(
    'messages',
    views.MessageViewSet,
    base_name='room-messages',
    parents_query_lookups=['room']
)


urlpatterns = [
    path('', include(router.urls)),
]
