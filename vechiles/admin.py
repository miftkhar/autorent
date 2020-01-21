from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from django.contrib.auth.models import Group
from . import models
from . import forms

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

from imagekit.admin import AdminThumbnail


admin.site.site_header = 'Rent A Car System'

admin.site.unregister(Group)


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    fields = ('country', 'name')
    autocomplete_fields = ('country',)
    list_display = ('name', 'country')
    list_filter = ('name',)
    search_fields = ('name',)

    # fieldsets = (
    #     (None, {
    #         'fields': ('name', )
    #     }),
    #     ('Availability', {
    #         'fields': ('country',)
    #     }),
    # )


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    autocomplete_fields = ('state',)
    list_display = ('name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)

    # list_select_related = (
    #     'state',
    # )


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    autocomplete_fields = ('city',)
    list_display = ('name', 'city', 'get_city')
    list_filter = ('city',)
    search_fields = ('name',)

    def get_city(self, obj):
        return obj.city.state
    get_city.admin_order_field = 'city'
    get_city.short_description = 'State'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name', 'description', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)


@admin.register(models.BodyColor)
class BodyColorAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name', 'rgbhex')
    search_fields = ('name',)


@admin.register(models.EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Make)
class MakeAdmin(admin.ModelAdmin):
    autocomplete_fields = ('category',)
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name', 'get_cat')
    # list_filter = ('get_cat',)
    search_fields = ('name',)

    def get_cat(self, obj):
        return obj.category.name
    # get_cat.admin_order_field = 'category'
    #
    get_cat.short_description = 'Category'


@admin.register(models.VModel)
class VModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('make',)
    # raw_id_fields = ('make',)
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name', 'get_make')
    # list_filter = ('get_make',)
    search_fields = ('name', 'make__name')
    short_description = 'iftkhar'

    def get_make(self, obj):
        return obj.make.name
    # get_make.admin_order_field = 'category'
    get_make.short_description = 'Make'


@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    fields = ('name', 'model', 'year', 'date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    autocomplete_fields = ('model',)
    list_display = ('name', 'get_model', 'year', 'get_make')
    list_filter = ('model__make__name',)
    search_fields = ('name', 'year')
    short_description = 'iftkhar'

    # fieldsets = (
    #     ('Required Information', {
    #         'description': "These fields are required.",
    #         'fields': (('name','model'),'year')
    #     }),
    #     ('Optional Information', {
    #         'classes': ('collapse',),
    #         'fields': ()
    #     }),
    # )

    def get_model(self, obj):
        return obj.model.name
    # get_model.admin_order_field = 'category'
    #
    get_model.short_description = 'Model'

    def get_make(self, obj):
        return obj.model.make.name
    # get_make.admin_order_field = 'category'
    #
    get_make.short_description = 'Make'


@admin.register(models.CarFeature)
class CarFeatureAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('car', 'feature',)
    #search_fields = ('name',)


class InlineCarFeature(admin.TabularInline):
    model = models.CarFeature
    form = forms.FeatureForm
    list_display = ('car', 'feature',)
    exclude = ('date_added', 'date_modified',)
    #admin_thumbnail = AdminThumbnail(image_field='image_100_50')
    #readonly_fields = ('admin_thumbnail', )


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    autocomplete_fields = ('category',)
    readonly_fields = ('date_added', 'date_modified')
    list_display = ('name', 'get_cat')
    # list_filter = ('get_cat',)
    search_fields = ('name', 'category__name')

    def get_cat(self, obj):
        return obj.category.name
    get_cat.short_description = 'Make'


class InlineImage(admin.TabularInline):
    model = models.Image
    list_display = ('name', 'title', 'admin_thumbnail',)
    exclude = ('date_added', 'date_modified',)
    admin_thumbnail = AdminThumbnail(image_field='image_100_50')
    admin_thumbnail.short_description = 'Image'
    readonly_fields = ('date_added', 'date_modified',)

    @mark_safe
    def image_tag(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" />'.format(obj.image_file.url))
        else:
            return 'No_image'

    image_tag.short_description = 'Image'


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):

    raw_id_fields = ('version',)
    form = forms.CarForm
    autocomplete_fields = ('location',)
    readonly_fields = ('date_added', 'date_modified', 'car_slug')
    # save_on_top = True
    # fields = ('car_slug',)
    list_display = ('title', 'bodycolor', 'car_slug')
    list_filter = ('make', 'model__name')
    # search_fields = ('name', 'version__model__make__name')

    list_select_related = (
        'bodycolor', 'bodytype'
    )

    inlines = [InlineImage, InlineCarFeature]

    fieldsets = (
        ('Required Info', {
            # 'description': "These fields are required.'make', 'model',",
            'fields': ('user', 'make', 'model', 'version', 'bodycolor', 'bodytype',
                       'transmission', 'enginetype', 'registration_city',
                       'title',  'price', 'condition', 'engine_capacity', 'is_active'
                       ),
            'classes': ('baton-tabs-init', 'baton-tab-fs-other', 'baton-tab-inline-images', 'baton-tab-inline-carfeature', ),
            'description': 'This is a description text'

        }),
        ('Other Info', {
            # 'classes': ('collapse',),
            'fields': (
                'location',
                'description',
                'mileage',
                'is_imported',
                'activation_admin',
                'date_added',
                'date_modified',
            ),
            'classes': ('tab-fs-other', ),
        }),
    )

    class Media:
        js = (
            'admin/stuff.js',
        )

    # class Media:
    #     #js = ('js/admin/my_own_admin.js',)
    #     css = {
    #         'all': ('vechiles/custom.css',)
    #     }

    # def get_user(self, obj):
    #     return obj.user.name
    # get_user.short_description = 'User'


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('name', 'title', 'admin_thumbnail')
    search_fields = ('name',)
    admin_thumbnail = AdminThumbnail(image_field='image_100_50')
    admin_thumbnail.short_description = 'Image'
    readonly_fields = ('date_added', 'date_modified',)

    def image_thumbnail(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image_100_50.url,
            width=obj.image_100_50.width,
            height=obj.image_100_50.height,
        )
        )

    @mark_safe
    def image_tag(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" />'.format(obj.image_file.url))
        else:
            return 'No_image'

    image_tag.short_description = 'Image'
