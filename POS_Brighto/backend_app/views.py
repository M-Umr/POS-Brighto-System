from rest_framework import mixins, viewsets

from .models import POS_Table
from .serializers import POSSerializer


class POSViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = POS_Table.objects.all()

    def get_serializer_class(self):
        return POSSerializer
