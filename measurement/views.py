# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializerWithSensor


class SensorList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializerWithSensor
