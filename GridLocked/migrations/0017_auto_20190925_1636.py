# Generated by Django 2.2.5 on 2019-09-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GridLocked', '0016_auto_20190925_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='strong_vs',
        ),
        migrations.AddField(
            model_name='fighter',
            name='tough_vs',
            field=models.ManyToManyField(blank=True, related_name='_fighter_tough_vs_+', to='GridLocked.Attribute'),
        ),
    ]
