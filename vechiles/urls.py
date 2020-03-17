from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
#from cruds_adminlte.urls import crud_for_app

urlpatterns = [
    path('country/<int:pk>/', views.CountryDetailView.as_view()),
    path('country/', views.CountryListView.as_view()),
    path('state/', views.StateListView.as_view()),
    path('city/', views.CityListView.as_view()),
    path('location/', views.LocationListView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path('make/', views.MakeListView.as_view()),
    path('model/', views.VModelListView.as_view()),
    path('version/', views.VersionListView.as_view()),
    path('bodytype/', views.BodyTypeListView.as_view()),
    path('bodycolor/', views.BodyColorListView.as_view()),
    path('enginetype/', views.EngineTypeListView.as_view()),
    path('transmission/', views.TransmissionListView.as_view()),
    path('feature/', views.FeatureListView.as_view()),
    path('carfeature/', views.CarFeatureListView.as_view()),
    path('user-car/', views.UserCarListView.as_view(), name='user-car'),
    path('user-car/<int:pk>', views.UserCarDetailView.as_view(), name='user-car'),
    path('user-car-image/', views.UserCarImageListView.as_view(),
         name='user-car-image'),
    path('user-car-feature/<int:pk>/', views.UserCarFeatureListView.as_view(),
         name='user-car-feature'),
    path('car/', views.CarListView.as_view(), name='car'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car'),
    path('city-autocomplete/', views.CityAutocomplete.as_view(),
         name='city-autocomplete'),
    path('state-autocomplete/', views.StateAutocomplete.as_view(),
         name='state-autocomplete'),
    path('version-autocomplete/', views.VersionAutocomplete.as_view(),
         name='version-autocomplete'),
    path('make-autocomplete/', views.MakeAutocomplete.as_view(),
         name='make-autocomplete'),
    path('model-autocomplete/', views.ModelAutocomplete.as_view(),
         name='model-autocomplete'),
    #path('<int:pk>/', views.UserDetailView.as_view()),

]

#urlpatterns += crud_for_app('vechiles')
