
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('gameapp.urls')),
    path('user/', include('userapp.urls'))
]
