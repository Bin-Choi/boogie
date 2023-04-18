from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/movies/', include('movies.urls')),
    path('api/community/', include('community.urls')),
    path('api/users/', include('accounts.urls')),
    path('api/accounts/', include('dj_rest_auth.urls')),
    path('api/accounts/signup/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
