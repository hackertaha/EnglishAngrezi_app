from django.contrib import admin
from django.urls import path
from django.conf import settings
from englishAngrezi import views
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', views.index, name='index'),
    path('admin/', admin.site.urls),
]