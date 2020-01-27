from django_filters import rest_framework as filters
from . import models


class VersionFilter(filters.FilterSet):
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    model_name = filters.CharFilter(
        field_name='model__name', label="Search by model name")
    make_name = filters.CharFilter(
        field_name='model__make__name', lookup_expr='icontains', label="Search by make name")

    class Meta:
        model = models.Version
        fields = ['id', 'model', 'model_name', 'make_name']


class CarFilter(filters.FilterSet):
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    model_name = filters.CharFilter(
        field_name='model__name', label="Search by model name")
    make_name = filters.CharFilter(
        field_name='model__make__name', lookup_expr='icontains', label="Search by make name")
    city = filters.CharFilter(
        field_name='registration_city', label="Search by city name")

    class Meta:
        model = models.Car
        fields = ['make', 'model', 'version', 'city']
