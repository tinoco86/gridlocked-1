# Generated by Django 2.2.5 on 2019-10-08 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GridLocked', '0018_auto_20190927_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]