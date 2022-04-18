from rest_framework.decorators import api_view
from .services import ListingService, NotificationService
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def get_listing(request):
    return Response(ListingService.get_listing(request.data), status=status.HTTP_200_OK)


@api_view(['GET'])
def retrieve_notifications(request):
    return Response(NotificationService.retrieve_notifications(), status=status.HTTP_200_OK)
