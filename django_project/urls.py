from django.contrib import admin
from django.urls import path
from example.views import mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView),
]
