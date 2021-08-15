from io import StringIO
from django.core.management import call_command
from django.test import TestCase
import pytest
from ..models import Card, Tags

pytestmark = pytest.mark.django_db

# def check_duplicate_cards():
#     try:
#         Card.objects.raw('''
#             select * from insights_tags tg
#             where (select count(*) from insights_tags tg2
#             where tg.name = tg2.name) > 1''')[0]
#         return True
#     except:
#         return False


class CommandTest(TestCase):
    def test_load_csv_validate_command_output(self):

        call_command("load_csv_validate")
        self.assertEqual(True, Card.objects.all().exists())

    def test_load_csv_command_output(self):
        call_command("load_csv")
        self.assertEqual(True, Card.objects.all().exists())
