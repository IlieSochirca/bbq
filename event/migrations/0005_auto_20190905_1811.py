# Generated by Django 2.1.7 on 2019-09-05 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20190905_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Organizer', to=settings.AUTH_USER_MODEL),
        ),
    ]
