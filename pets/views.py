from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Pet
from .serializers import PetSerializer
from accounts.permissions import IsAdminOrReadOnly


class PetListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all().order_by("-created_at")
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):

        queryset = Pet.objects.all().order_by("-created_at")

        search = self.request.query_params.get("search")
        animal_type = self.request.query_params.get("animal_type")
        breed = self.request.query_params.get("breed")
        gender = self.request.query_params.get("gender")
        location = self.request.query_params.get("location")
        status = self.request.query_params.get("status")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if animal_type:
            queryset = queryset.filter(animal_type__iexact=animal_type)

        if breed:
            queryset = queryset.filter(breed__icontains=breed)

        if gender:
            queryset = queryset.filter(gender__iexact=gender)

        if location:
            queryset = queryset.filter(location__icontains=location)

        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset


class PetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrReadOnly]