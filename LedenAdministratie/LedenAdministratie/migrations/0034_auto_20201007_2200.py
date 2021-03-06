# Generated by Django 2.1.5 on 2019-02-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LedenAdministratie', '0033_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='scouting_nr',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='member',
            name='t-shirt',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='member',
            name='jub-badge',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='member',
            name='verzekering',
            field=models.CharField(max_length=40),

        ),
        migrations.AddField(
            model_name='member',
            name='foto_publiek',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='foto_intern',
            field=models.BooleanField(default=False),
        ),
    ]
