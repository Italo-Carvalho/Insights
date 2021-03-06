from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializes
from insights import models
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
    queryset = models.Card.objects.all().prefetch_related("tags")
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("tags",)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializes.CardSerializerList
        else:
            return serializes.CardSerializer


class CardViewsetsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Card.objects.all().prefetch_related("tags")
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.CardSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializes.CardSerializerList
        else:
            return serializes.CardSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializes.UserSerializer
