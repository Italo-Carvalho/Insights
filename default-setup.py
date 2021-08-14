#!/usr/bin/env python

from insights.models import CustomUser
from django.core.management import call_command

CustomUser.objects.create_superuser('test@test.com', 'test123')
call_command('load_csv')