from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('name',)
        #fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = ('name',)


class CitySerializer(serializers.ModelSerializer):

    state_name = serializers.ReadOnlyField(source='state.name')

    #car = serializers.SerializerMethodField(read_only=True)

    city_total = serializers.SerializerMethodField(read_only=True)
    registered_total = serializers.SerializerMethodField(read_only=True)

    def get_city_total(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.carCity.count()

    def get_registered_total(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.car.count()

    class Meta:
        model = models.City
        fields = ('id', 'name', 'state_name', 'city_total', 'registered_total')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('name', 'city', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name',)


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BodyType
        fields = ('name', 'description')


class BodyColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BodyColor
        fields = ('name', 'rgbhex')


class EngineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EngineType
        fields = ('name',)


class TransmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transmission
        fields = ('name',)


class MakeSerializer(serializers.ModelSerializer):
    total_car = serializers.SerializerMethodField(read_only=True)

    def get_total_car(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.car.count()

    class Meta:
        model = models.Make
        fields = ('id', 'name', 'total_car',)


class FeatureSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Feature
        fields = ('name', 'category_name',)


class VersionSerializer(serializers.ModelSerializer):
    model_name = serializers.ReadOnlyField(source='model.name')
    make_name = serializers.ReadOnlyField(source='model.make.name')
    make = serializers.ReadOnlyField(source='model.make.id')
    total_car = serializers.SerializerMethodField(read_only=True)

    def get_total_car(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.car.count()

    class Meta:
        model = models.Version
        fields = ('id', 'name', 'model', 'model_name',
                  'make', 'make_name', 'year', 'total_car')


class VModelSerializer(serializers.ModelSerializer):
    make_name = serializers.ReadOnlyField(source='make.name')
    total_car = serializers.SerializerMethodField(read_only=True)

    def get_total_car(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.car.count()

    class Meta:
        model = models.VModel
        fields = ('id', 'name', 'make', 'make_name', 'is_popular', 'total_car')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'


class CarFeatureSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='feature.name')
    #id = serializers.ReadOnlyField(source='feature.id')

    class Meta:
        model = models.CarFeature
        fields = '__all__'
        fields = ('id', 'is_active', 'name',)
        #depth = 1


class CarSerializer(serializers.ModelSerializer):

    version_name = serializers.ReadOnlyField(source='version.name')
    model_name = serializers.ReadOnlyField(source='model.name')
    make_name = serializers.ReadOnlyField(source='make.name')
    city_name = serializers.ReadOnlyField(source='city.name')
    bodycolor_name = serializers.ReadOnlyField(source='bodycolor.name')
    bodytype_name = serializers.ReadOnlyField(source='bodytype.name')
    transmission_name = serializers.ReadOnlyField(source='transmission.name')
    enginetype_name = serializers.ReadOnlyField(source='enginetype.name')
    registration_city_name = serializers.ReadOnlyField(
        source='registration_city.name')
    location_name = serializers.ReadOnlyField(source='location.name')

    condition = serializers.CharField(source='get_condition_display')
    images = ImageSerializer(required=False, many=True)
    #feature = CarFeatureSerializer(required=False, many=True)
    carfeatures = CarFeatureSerializer(
        source='car_features', many=True, read_only=True)
    #registration_city = serializers.CharField(source='registration_city.name')
    #features = serializers.ManyRelatedField(source='features.name')

    class Meta:
        model = models.Car
        fields = ('id','title', 'description', 'price',
                  'version', 'version_name',
                  'model', 'model_name',
                  'make', 'make_name',
                  'city', 'city_name',
                  'bodycolor', 'bodycolor_name',
                  'bodytype', 'bodytype_name',
                  'transmission', 'transmission_name',
                  'enginetype', 'enginetype_name', 'engine_capacity',
                  'registration_city', 'registration_city_name',
                  'location', 'location_name',
                  'mileage', 'condition',
                  'is_featured', 'is_verified', 'is_with_driver_only', 'is_imported',
                  'carfeatures', 'images',
                  )
        #fields = '__all__'
