# from django_filters.rest_framework import DjangoFilterBackend

from django.urls import reverse, resolve
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import connection
from django.db.models import Q
from dal import autocomplete
from . import models
from . import serializers
from . import filters


class CountryListView(generics.ListCreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    filterset_fields = ('name',)


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class StateListView(generics.ListCreateAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CityListView(generics.ListCreateAPIView):

    #queryset = models.City.objects.all().prefetch_related('car', 'state')
    serializer_class = serializers.CitySerializer
    #filterset_fields = ('name', 'id', 'state__id', 'state__name')

    def get_queryset(self):
        queryset = models.City.objects.all().prefetch_related('car', 'state')
        city = self.request.query_params.get('city', None)
        make = self.request.query_params.get('make', None)
        model = self.request.query_params.get('model', None)
        version = self.request.query_params.get('version', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if city is not None:
            queryset = queryset.filter(id=city)
        if model is not None:
            queryset = queryset.filter(car__model=model)
        if make is not None:
            queryset = queryset.filter(car__make=make)
        if version is not None:
            queryset = queryset.filter(car__version=version)
        if min_price is not None:
            queryset = queryset.filter(car__price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(car__price__lte=max_price)
            #queryset = models.Car.objects.filter(Q(model=336) or Q(make=5))
        return queryset
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


class VersionListView(generics.ListCreateAPIView):

    serializer_class = serializers.VersionSerializer
    queryset = models.Version.objects.all().prefetch_related('model', 'model__make')
    filterset_class = filters.VersionFilter
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
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    # filterset_class = filters.CarFilter

    def get_queryset(self):
        queryset = models.Car.objects.all()
        make = self.request.query_params.get('make', None)
        model = self.request.query_params.get('model', None)
        version = self.request.query_params.get('version', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if model is not None:
            queryset = queryset.filter(model=model)
        if make is not None:
            queryset = queryset.filter(make=make)
        if version is not None:
            queryset = queryset.filter(version=version)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        #queryset = models.Car.objects.filter(Q(model=336) or Q(make=5))
        return queryset


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
