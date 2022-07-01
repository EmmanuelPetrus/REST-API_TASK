from django.shortcuts import render

from I4G011631AAD.links.serializer import LinkSerializer
from .models import Link
from .serializer import LinkSerializer
from rest_framework.generics import ListAPIView
# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer


