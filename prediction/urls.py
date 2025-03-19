from django.urls import path
from .views import water_quality_prediction

urlpatterns = [
    path("predict/", water_quality_prediction, name="water_quality_prediction"),
]