from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import permission_classes


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed
    """
    queryset = Group.objects.all()
    serializer_class = CoreGroupSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ProjectGroups
    """
    queryset = Project.objects.filter(isActive=True)
    serializer_class = ProjectGroupSerializer