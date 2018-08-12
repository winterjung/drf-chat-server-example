from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.chat import views


router = NestedDefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
