from django.urls import include, path
from django.contrib import admin

# define urls here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
