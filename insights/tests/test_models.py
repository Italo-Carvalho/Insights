import pytest
from insights.models import CustomUser, Tags, Card
from django.test import TestCase

pytestmark = pytest.mark.django_db


class ModelTest(TestCase):
    def test_create_customuser(self):
        user = CustomUser.objects.create(
            email="pytestdjango@django.com", password="passw0rd"
        )

        assert user.email == "pytestdjango@django.com"
        assert user.__str__() == "pytestdjango@django.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email="admin@test.com", password="passw0rd"
        )
        assert user.email == "admin@test.com"
        assert user.is_active
        assert user.is_staff
        assert user.is_superuser

    def test_create_user_errors(self):
        with pytest.raises(ValueError) as user_create:
            CustomUser.objects.create_superuser(email="", password="passw0rd")

        with pytest.raises(ValueError) as super_user_create_staff:
            CustomUser.objects.create_superuser(
                email="test@test.com", password="passw0rd", is_staff=False
            )

        with pytest.raises(ValueError) as super_user_create_superuser:
            CustomUser.objects.create_superuser(
                email="test@test.com", password="passw0rd", is_superuser=False
            )

        assert user_create.value.args[0] == "O e-mail deve ser definido"
        assert (
            super_user_create_staff.value.args[0]
            == "O superusuário deve está is_staff=True."
        )
        assert (
            super_user_create_superuser.value.args[0]
            == "O superusuário deve está is_superuser=True."
        )

    def test_create_tag(self):
        tag = Tags.objects.create(name="test")
        assert tag.__str__() == "test"

    def test_create_card(self):
        card = Card.objects.create(texto="test")
        assert card.__str__() == "test"
