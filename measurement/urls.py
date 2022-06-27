from django.urls import path
from .views import SensorList, SensorUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
