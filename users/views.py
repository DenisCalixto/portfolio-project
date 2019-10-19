from django.shortcuts import render
from django.db.models import Q
from django.core import serializers
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer, UserDetailSerializer

import json


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @method_decorator(never_cache)
    @action(detail=False)
    def get_by_username(self, request):
        users = User.objects.filter(Q(username__exact=request.GET.get("username"))) \
                    .values('id', 'first_name', 'last_name', 'username', 'email', 'bio', 'picture')
        users_list = list(users)  # important: convert the QuerySet to a list object
        return JsonResponse(users_list[0], safe=False)
