from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tech.urls')),
    path('accounts/', include('allauth.urls')),

    # http://localhost:8000/accounts/github/login/callback/
]
