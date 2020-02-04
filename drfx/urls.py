from django.conf import settings
from django.contrib import admin
# from baton.autodiscover import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('baton/', include('baton.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('users/', include('users.urls')),
    path('api/v1/vehicles/', include('vechiles.urls')),
    #path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/user/', include('rest_auth.urls')),
    path('api/v1/user/registration/', include('rest_auth.registration.urls')),
    path('all-auth/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar  # Add debugging urls

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # Static Files URLS
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
