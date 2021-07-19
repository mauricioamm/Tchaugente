from django.contrib import admin
from django.urls import path
from TchaugenteApp.views import entrada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entrada, name='url_entrada'),
]