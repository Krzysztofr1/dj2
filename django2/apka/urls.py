from django.urls import path, include
from .views import index

urlpatterns = [
   path('', include('testapp.urls')),
   path('test/<int:id>/', index),
]
