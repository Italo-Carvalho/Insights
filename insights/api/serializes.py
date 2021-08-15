from django.db.models import fields
from rest_framework import serializers
from ..models import Tags, Card, CustomUser


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ("id", "name")


class CardSerializer(serializers.ModelSerializer):

    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tags.objects.all())

    class Meta:
        model = Card
        fields = ("id", "texto", "tags", "data_criacao", "data_modificacao")


class CardSerializerList(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = ("id", "texto", "data_criacao", "data_modificacao", "tags")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
