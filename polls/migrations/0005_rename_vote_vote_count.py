# Generated by Django 4.2.2 on 2023-07-25 11:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_vote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vote',
            new_name='Vote_count',
        ),
    ]
