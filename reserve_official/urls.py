from django.urls import path
from .views import get_listing, retrieve_notifications

urlpatterns = [
    path('listing/storeListing', get_listing),
    path('shared/notifications', retrieve_notifications),
]
