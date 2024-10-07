from django.urls import path
from .views import views1, views2

urlpatterns = [
    path("strona/",views1),
    path("strona/<int:id>/", views2)
]