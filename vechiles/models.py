from django.db import models
from users.models import CustomUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=True)
    #

    class Meta:
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


# Create your models here.
class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(
        'Country', related_name='country_name', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        ##managed = False
        db_table = 'state'

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(
        'State', related_name='state_name', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False, null=True)
    lat = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(
        'City', related_name='city_name', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=False, null=True)
    lat = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'location'

    def __str__(self):
        return "{}-{}".format(self.city, self.name)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=True)

    class Meta:
        ##managed = False
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class BodyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=1, verbose_name='Active')
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        ##managed = False
        db_table = 'body_type'
        verbose_name = 'Body Type'
        verbose_name_plural = 'Body Types'

    def __str__(self):
        return self.name


class BodyColor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    rgbhex = models.CharField(max_length=45, blank=False, null=False)
    is_active = models.BooleanField(default=1)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        ##managed = False
        db_table = 'body_color'
        verbose_name = 'Body Color'
        verbose_name_plural = 'Body Colors'

    def __str__(self):
        return self.name


class Transmission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=True)
    is_active = models.BooleanField(default=1)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        ##managed = False
        db_table = 'transmission'
        verbose_name = 'Transmission'
        verbose_name_plural = 'Transmissions'

    def __str__(self):
        return self.name


class EngineType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=True)
    is_active = models.BooleanField(default=1)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        ##managed = False
        db_table = 'engine_type'
        verbose_name = 'Engine Type'
        verbose_name_plural = 'Engine Types'

    def __str__(self):
        return self.name


class Make(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(unique=True, max_length=100,
                            blank=False, null=True)
    activated = models.BooleanField(blank=True, null=True)
    date_added = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)

    class Meta:
        #managed = False
        db_table = 'make'

    def __str__(self):
        return self.name


class VModel(models.Model):
    id = models.AutoField(primary_key=True)
    #category_id = models.IntegerField(blank=True, null=True)
    make = models.ForeignKey(Make, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False, null=True)
    # This field type is a guess.
    is_popular = models.BooleanField(default=False)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        #managed = False
        db_table = 'vmodel'
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name


class Version(models.Model):

    YEAR_CHOICES = []
    for r in range(1960, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    model = models.ForeignKey(VModel, on_delete=models.PROTECT)
    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.now().year)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        #managed = False
        db_table = 'version'

    def __str__(self):
        return self.name


class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(unique=True, max_length=255,
                            blank=False, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=1)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)

    class Meta:
        #managed = False
        db_table = 'feature'

    def __str__(self):
        return self.name


class Car(models.Model):

    EXCELLENT = 1
    VERY_GOOD = 2
    GOOD = 3
    FAIR = 4
    CONDITION_CHOICES = (
        (EXCELLENT, 'Excellent'),
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (FAIR, 'Fair')
    )

    id = models.BigAutoField(primary_key=True)
    version = models.ForeignKey('Version', on_delete=models.PROTECT, related_name='car')
    model = models.ForeignKey(
        'VModel', on_delete=models.PROTECT, related_name='car')
    make = models.ForeignKey(
        'Make', on_delete=models.PROTECT, related_name='car')
    user = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT)
    bodycolor = models.ForeignKey(
        'BodyColor', verbose_name='Color', on_delete=models.PROTECT)
    bodytype = models.ForeignKey('BodyType', on_delete=models.PROTECT)
    transmission = models.ForeignKey('Transmission', on_delete=models.PROTECT)
    enginetype = models.ForeignKey('EngineType', on_delete=models.PROTECT)
    registration_city = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name='car')
    location = models.ForeignKey(
        'Location', on_delete=models.PROTECT, blank=True, null=True)
    features = models.ManyToManyField(Feature, through='CarFeature')
    title = models.CharField(max_length=500, blank=False)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=False, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    condition = models.IntegerField(
        'condition', choices=CONDITION_CHOICES, default=VERY_GOOD)
    engine_capacity = models.IntegerField(blank=False, null=True)
    is_active = models.BooleanField(default=1)
    is_imported = models.BooleanField(default=0)
    is_featured = models.BooleanField(default=0)
    is_with_driver_only = models.BooleanField(default=0)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)
    nviews = models.BigIntegerField(default=0)
    activation_admin = models.BooleanField(default=1)

    class Meta:
        managed = True
        db_table = 'car'

    def __str__(self):
        return self.title

    def car_slug(self):
        return "{} {} {}".format(self.make, self.model, self.version)
    car_slug.short_description = 'Car'


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    car = models.ForeignKey(
        'Car', null=True, related_name='images', on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.ImageField(upload_to='media/images/')
    image_100_50 = ImageSpecField(source='image_file',
                                  processors=[ResizeToFill(100, 50)],
                                  format='JPEG',
                                  options={'quality': 60})
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)
    default_status = models.BooleanField(default=1)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        #managed = False
        db_table = 'image'

    def __str__(self):
        return str(self.name) if self.name else ''


class CarFeature(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(
        Car, db_index=False, on_delete=models.PROTECT)
    feature = models.ForeignKey(
        Feature, db_index=False, on_delete=models.PROTECT)
    date_added = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)
    is_active = models.BooleanField(default=1, verbose_name='Active Status')

    class Meta:
        #managed = False
        db_table = 'car_feature'
        unique_together = (
            'car',
            'feature'
        )
