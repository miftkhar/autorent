from django_filters import rest_framework as f
#from django_filters.rest_framework import FilterSet,
from . import models


class NumberInFilter(f.BaseInFilter, f.NumberFilter):
    pass


class NumberRangeFilter(f.BaseRangeFilter, f.NumberFilter):
    pass


class CityFilter(f.FilterSet):
    #min_price = NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = NumberFilter(field_name="price", lookup_expr='lte')
    # model_name = CharFilter(
    #     field_name='model__name', label="Search by model name")
    # make_name = CharFilter(
    #     field_name='model__make__name', lookup_expr='icontains', label="Search by make name")
    # make = NumberFilter(field_name='model__make__id')
    model = NumberInFilter(field_name='car__model', lookup_expr='in')
    make = NumberInFilter(field_name='car__make', lookup_expr='in')
    price = NumberRangeFilter(field_name='car__price', lookup_expr='range')

    class Meta:
        model = models.City
        fields = ['id', 'model', 'make', 'price']


class VersionFilter(f.FilterSet):
    #min_price = f.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = f.NumberFilter(field_name="price", lookup_expr='lte')
    model_name = f.CharFilter(
        field_name='model__name', label="Search by model name")
    make_name = f.CharFilter(
        field_name='model__make__name', lookup_expr='icontains', label="Search by make name")
    make = f.NumberFilter(field_name='model__make__id')

    class Meta:
        model = models.Version
        fields = ['id', 'model', 'make', 'model_name', 'make_name']


class CarFilter(f.FilterSet):
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    model_name = f.CharFilter(
        field_name='model__name', label="Search by model name")
    make_name = f.CharFilter(
        field_name='model__make__name', lookup_expr='icontains', label="Search by make name")
    city = f.CharFilter(
        field_name='registration_city', label="Search by city name")

    class Meta:
        model = models.Car
        fields = ['make', 'model', 'version', 'city']
