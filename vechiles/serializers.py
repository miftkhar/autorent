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
    class Meta:
        model = models.City
        fields = ('name', 'state')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('name', 'city')


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
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Make
        fields = ('name', 'category_name')


class FeatureSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Feature
        fields = ('name', 'category_name', 'featurecol')


class VersionSerializer(serializers.ModelSerializer):
    model_name = serializers.ReadOnlyField(source='model.name')
    make_name = serializers.ReadOnlyField(source='model.make.name')

    class Meta:
        model = models.Version
        fields = ('name', 'model_name', 'make_name', 'year')


class VModelSerializer(serializers.ModelSerializer):
    make_name = serializers.ReadOnlyField(source='make.name')

    class Meta:
        model = models.VModel
        fields = ('name', 'make_name', 'is_popular')


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
    #model_name = serializers.ReadOnlyField(source='model.name')
    #make_name = serializers.ReadOnlyField(source='model.make.name')
    images = ImageSerializer(required=False, many=True)
    #feature = CarFeatureSerializer(required=False, many=True)
    carfeatures = CarFeatureSerializer(
        source='carfeature_set', many=True, read_only=True)
    registration_city = serializers.CharField(source='registration_city.name')
    #features = serializers.ManyRelatedField(source='features.name')

    class Meta:
        model = models.Car
        #fields = ('name', 'model_name', 'make_name', 'year')
        fields = '__all__'
