from django.shortcuts import render
from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
