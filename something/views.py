from rest_framework import generics
from .models import Company, Cars
from .serializers import CompanySerializer, CarsSerializer

# Create your views here.

# INDEX, POST


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# SHOW, PUT, DELETE
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# INDEX, POST
class CarList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


# SHOW, PUT, DELETE
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
