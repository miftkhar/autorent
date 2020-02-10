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

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class StateListView(generics.ListCreateAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class CityListView(generics.ListCreateAPIView):

    #queryset = models.City.objects.all().prefetch_related('car', 'state')
    #queryset = models.City.objects.all().prefetch_related('car', 'carCity', 'state')
    serializer_class = serializers.CitySerializer
    #filterset_class = filters.CityFilter
    #pagination_class = None
    #filterset_fields = ('name', 'id', 'state__id', 'state__name')

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_queryset(self):
        queryset = models.City.objects.all().prefetch_related('car', 'carCity', 'state')
        city = self.request.query_params.get('city', None)
        make = self.request.query_params.get('make', None)
        model = self.request.query_params.get('model', None)
        version = self.request.query_params.get('version', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        # create an empty list for parameters to be filters by
        cityParams = []
        modalParams = []
        makeParams = []
        versionParams = []

        if city is not None:
            for i in city.split(','):
                cityParams.append(int(i))
            if len(cityParams) > 1:
                queryset = queryset.filter(id__in=cityParams)
            else:
                queryset = queryset.filter(id=city)

        if model is not None:
            for i in model.split(','):
                modalParams.append(int(i))
            if len(modalParams) > 1:
                queryset = queryset.filter(car__model__in=modalParams)
            else:
                queryset = queryset.filter(car__model=model)

        if make is not None:
            for i in make.split(','):
                makeParams.append(int(i))
            if len(makeParams) > 1:
                queryset = queryset.filter(car__make__in=makeParams)
            else:
                queryset = queryset.filter(car__make=make)

        if version is not None:
            for i in version.split(','):
                versionParams.append(int(i))
            if len(versionParams) > 1:
                queryset = queryset.filter(car__version__in=versionParams)
            else:
                queryset = queryset.filter(car__version=version)

        if min_price is not None:
            queryset = queryset.filter(car__price__gte=min_price)
            #queryset = queryset.filter(Q(car__price__gte=min_price))
        if max_price is not None:
            queryset = queryset.filter(car__price__lte=max_price)
            #queryset = queryset.filter(Q(car__price__lte=max_price))
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

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_queryset(self):
        queryset = models.Location.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class BodyTypeListView(generics.ListCreateAPIView):
    queryset = models.BodyType.objects.all()
    serializer_class = serializers.BodyTypeSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class BodyColorListView(generics.ListCreateAPIView):
    queryset = models.BodyColor.objects.all()
    serializer_class = serializers.BodyColorSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class EngineTypeListView(generics.ListCreateAPIView):
    queryset = models.EngineType.objects.all()
    serializer_class = serializers.EngineTypeSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class TransmissionListView(generics.ListCreateAPIView):
    queryset = models.Transmission.objects.all()
    serializer_class = serializers.TransmissionSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class MakeListView(generics.ListCreateAPIView):

    serializer_class = serializers.MakeSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_queryset(self):
        queryset = models.Make.objects.all().prefetch_related('car',)
        city = self.request.query_params.get('city', None)
        make = self.request.query_params.get('make', None)
        model = self.request.query_params.get('model', None)
        version = self.request.query_params.get('version', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        # create an empty list for parameters to be filters by
        cityParams = []
        modalParams = []
        makeParams = []
        versionParams = []

        if city is not None:
            for i in city.split(','):
                cityParams.append(int(i))
            if len(cityParams) > 1:
                queryset = queryset.filter(car__city__in=cityParams)
            else:
                queryset = queryset.filter(car__city=city)

        if model is not None:
            for i in model.split(','):
                modalParams.append(int(i))
            if len(modalParams) > 1:
                queryset = queryset.filter(car__model__in=modalParams)
            else:
                queryset = queryset.filter(car__model=model)

        if make is not None:
            for i in make.split(','):
                makeParams.append(int(i))
            if len(makeParams) > 1:
                queryset = queryset.filter(id__in=makeParams)
            else:
                queryset = queryset.filter(id=make)

        if version is not None:
            for i in version.split(','):
                versionParams.append(int(i))
            if len(versionParams) > 1:
                queryset = queryset.filter(car__version__in=versionParams)
            else:
                queryset = queryset.filter(car__version=version)

        if min_price is not None:
            #queryset = queryset.filter(car__price__gte=min_price)
            queryset = queryset.filter(Q(car__price__gte=min_price))
        if max_price is not None:
            #queryset = queryset.filter(car__price__lte=max_price)
            queryset = queryset.filter(Q(car__price__lte=max_price))
            #queryset = models.Car.objects.filter(Q(model=336) or Q(make=5))
        return queryset


class VModelListView(generics.ListCreateAPIView):

    serializer_class = serializers.VModelSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_queryset(self):
        queryset = models.VModel.objects.all().prefetch_related('make', 'car')
        make = self.request.query_params.get('make', None)
        if make is not None:
            queryset = queryset.filter(make=make)
        return queryset


class FeatureListView(generics.ListCreateAPIView):

    serializer_class = serializers.FeatureSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_queryset(self):
        queryset = models.Feature.objects.all()
        cat = self.request.query_params.get('cat', None)
        if cat is not None:
            queryset = queryset.filter(category__name__contains=cat)
        return queryset


class VersionListView(generics.ListCreateAPIView):

    serializer_class = serializers.VersionSerializer
    queryset = models.Version.objects.all().prefetch_related(
        'model', 'model__make', 'car')
    filterset_class = filters.VersionFilter

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    #from django.core.mail import send_mail

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
    #queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    # filterset_class = filters.CarFilter

    def get_queryset(self):
        queryset = models.Car.objects.select_related(
            'version', 'model', 'make', 'bodycolor',
            'bodytype', 'transmission', 'enginetype', 'registration_city',
            'city', 'location',).prefetch_related('images', 'car_features',).all()
        city = self.request.query_params.get('city', None)
        make = self.request.query_params.get('make', None)
        model = self.request.query_params.get('model', None)
        version = self.request.query_params.get('version', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        # create an empty list for parameters to be filters by
        cityParams = []
        modalParams = []
        makeParams = []
        versionParams = []

        if city is not None:
            for i in city.split(','):
                cityParams.append(int(i))
            if len(cityParams) > 1:
                queryset = queryset.filter(city__in=cityParams)
            else:
                queryset = queryset.filter(city=city)

        if model is not None:
            for i in model.split(','):
                modalParams.append(int(i))
            if len(modalParams) > 1:
                queryset = queryset.filter(model__in=modalParams)
            else:
                queryset = queryset.filter(model=model)

        if make is not None:
            for i in make.split(','):
                makeParams.append(int(i))
            if len(makeParams) > 1:
                queryset = queryset.filter(make__in=makeParams)
            else:
                queryset = queryset.filter(make=make)

        if version is not None:
            for i in version.split(','):
                versionParams.append(int(i))
            if len(versionParams) > 1:
                queryset = queryset.filter(version__in=versionParams)
            else:
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
