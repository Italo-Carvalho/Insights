from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializes
from .. import models
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class TagsViewsetsC(generics.CreateAPIView):
    queryset = models.Tags.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.TagsSerializer

class TagsViewsetsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tags.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.TagsSerializer


class CardViewsetsLC(generics.ListCreateAPIView):
    queryset = models.Card.objects.all().prefetch_related('tags')
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.CardSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tags',)

class CardViewsetsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Card.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.CardSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializes.UserSerializer
