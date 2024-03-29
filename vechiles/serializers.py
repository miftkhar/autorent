from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('id', 'name',)
        #fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = ('id', 'name',)


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
        fields = ('id', 'name', 'city', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name',)


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BodyType
        fields = ('id', 'name', 'description')


class BodyColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BodyColor
        fields = ('id', 'name', 'rgbhex')


class EngineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EngineType
        fields = ('id', 'name',)


class TransmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transmission
        fields = ('id', 'name',)


class MakeSerializer(serializers.ModelSerializer):
    total_car = serializers.SerializerMethodField(read_only=True)

    def get_total_car(self, obj):
        # change 'car' with corresponding "related_name" value
        return obj.car.count()

    class Meta:
        model = models.Make
        fields = ('id', 'name', 'total_car',)
        depth = 1


class FeatureSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Feature
        fields = ('id', 'name', 'category_name',)


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


class ImageListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        Images = [models.Image(**item) for item in validated_data]
        return models.Image.objects.bulk_create(Images)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = ('id', 'car', 'title', 'image_file',)
        #list_serializer_class = ImageListSerializer


class CarFeatureSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='feature.name')
    #id = serializers.ReadOnlyField(source='feature.id')

    class Meta:
        model = models.CarFeature
        fields = ('id', 'is_active', 'name', 'car', 'feature')
        #depth = 1


class CarSerializer(serializers.ModelSerializer):

    version_name = serializers.ReadOnlyField(source='version.name')
    model_name = serializers.ReadOnlyField(source='model.name')
    make_name = serializers.ReadOnlyField(source='make.name')
    #city_name = serializers.ReadOnlyField(source='city.name')
    bodycolor_name = serializers.ReadOnlyField(source='bodycolor.name')
    bodytype_name = serializers.ReadOnlyField(source='bodytype.name')
    transmission_name = serializers.ReadOnlyField(source='transmission.name')
    enginetype_name = serializers.ReadOnlyField(source='enginetype.name')
    # registration_city_name = serializers.ReadOnlyField(
    #     source='registration_city.name')
    location_name = serializers.ReadOnlyField(source='location.name')

    condition = serializers.ReadOnlyField(source='get_condition_display')
    images = ImageSerializer(read_only=True, required=False, many=True)
    #feature = CarFeatureSerializer(required=False, many=True)
    carfeatures = CarFeatureSerializer(
        source='car_features', many=True, read_only=True, required=False)
    #registration_city = serializers.CharField(source='registration_city.name')
    #features = serializers.ManyRelatedField(source='features.name')

    class Meta:
        model = models.Car
        fields = ('id', 'title', 'description', 'price',
                  'version', 'version_name',
                  'model', 'model_name',
                  'make', 'make_name',
                  # 'city',
                  # 'city_name',
                  'price',
                  'bodycolor', 'bodycolor_name',
                  'bodytype', 'bodytype_name',
                  'transmission', 'transmission_name',
                  'enginetype', 'enginetype_name', 'engine_capacity',
                  #'registration_city', 'registration_city_name',
                  'location', 'location_name',
                  'mileage', 'condition',
                  'is_featured', 'is_verified', 'is_with_driver_only', 'is_imported',
                  'carfeatures',
                  'images',
                  )
        #fields = '__all__'

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
