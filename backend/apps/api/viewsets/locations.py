from rest_framework.viewsets import ReadOnlyModelViewSet
from iranian_cities.models import Province, City

from ..serializers.locations import OstanSerializer, ShahrSerializer


class ShahrViewset(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = ShahrSerializer


class OstanViewset(ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = OstanSerializer
