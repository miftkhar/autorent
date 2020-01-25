#from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from django.urls import reverse, resolve
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import connection
from dal import autocomplete
from . import models
from . import serializers


class CountryListView(generics.ListCreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('name',)


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class StateListView(generics.ListCreateAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CityListView(generics.ListCreateAPIView):

    queryset = models.City.objects.all().prefetch_related('car', 'state')

    serializer_class = serializers.CitySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('name', 'id', 'state__id', 'state__name')

    # def get_queryset(self):
    #     queryset = models.City.objects.all()
    #     state = self.request.query_params.get('state', None)
    #     if state is not None:
    #         queryset = queryset.filter(state__name__contains=state)
    #     return queryset


class LocationListView(generics.ListCreateAPIView):

    serializer_class = serializers.LocationSerializer

    def get_queryset(self):
        queryset = models.Location.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city__name__contains=city)
        return queryset


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BodyTypeListView(generics.ListCreateAPIView):
    queryset = models.BodyType.objects.all()
    serializer_class = serializers.BodyTypeSerializer


class BodyColorListView(generics.ListCreateAPIView):
    queryset = models.BodyColor.objects.all()
    serializer_class = serializers.BodyColorSerializer


class EngineTypeListView(generics.ListCreateAPIView):
    queryset = models.EngineType.objects.all()
    serializer_class = serializers.EngineTypeSerializer


class TransmissionListView(generics.ListCreateAPIView):
    queryset = models.Transmission.objects.all()
    serializer_class = serializers.TransmissionSerializer


class MakeListView(generics.ListCreateAPIView):

    serializer_class = serializers.MakeSerializer

    def get_queryset(self):
        queryset = models.Make.objects.all().prefetch_related('category')
        cat = self.request.query_params.get('cat', None)
        if cat is not None:
            queryset = queryset.filter(category__name__contains=cat)
        return queryset


class VModelListView(generics.ListCreateAPIView):

    serializer_class = serializers.VModelSerializer

    def get_queryset(self):
        queryset = models.VModel.objects.all().prefetch_related('make')
        make = self.request.query_params.get('make', None)
        if make is not None:
            queryset = queryset.filter(make__name__contains=make)
        return queryset


class FeatureListView(generics.ListCreateAPIView):

    serializer_class = serializers.FeatureSerializer

    def get_queryset(self):
        queryset = models.Feature.objects.all()
        cat = self.request.query_params.get('cat', None)
        if cat is not None:
            queryset = queryset.filter(category__name__contains=cat)
        return queryset


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


class VersionListView(generics.ListCreateAPIView):

    serializer_class = serializers.VersionSerializer
    queryset = models.Version.objects.all().prefetch_related('model', 'model__make')
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = VersionFilter
    # from django.core.mail import send_mail

    # send_mail('subject', 'body of the message',
    #           'ifyraj@gmail.com', ['ifyraj@gmail.com', ])
    # print('iftkhar')

    # def get_queryset(self):
    #     queryset = models.Version.objects.all().prefetch_related('model', 'model__make')
    #     vmodel = self.request.query_params.get('model', None)
    #     make = self.request.query_params.get('make', None)
    #     if vmodel is not None:
    #         queryset = queryset.filter(model__name__contains=vmodel)
    #     elif make is not None:
    #         queryset = queryset.filter(model__make__name__contains=make)
    #     return queryset


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


class CarListView(generics.ListCreateAPIView):
    queryset = models.Car.objects.all().prefetch_related('features')
    serializer_class = serializers.CarSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('version', 'model',)


class UserCarListView(generics.ListCreateAPIView):
    serializer_class = serializers.CarSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return models.Car.objects.filter(user=user)


class StateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.State.objects.all()
        return qs


class MakeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Make.objects.all()
        return qs


class ModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.is_authenticated():
        #     return models.City.objects.none()
        qs = models.VModel.objects.all()
        make = self.forwarded.get('make', None)
        if make:
            qs = qs.filter(make=make)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class VersionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.is_authenticated():
        #     return models.City.objects.none()
        qs = models.Version.objects.all()
        model = self.forwarded.get('model', None)
        if model:
            qs = qs.filter(model=model)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.is_authenticated():
        #     return models.City.objects.none()
        qs = models.City.objects.all()
        state = self.forwarded.get('src_state', None)
        if state:
            qs = qs.filter(state=state)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
