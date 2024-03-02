from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

class BaseListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class BaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    