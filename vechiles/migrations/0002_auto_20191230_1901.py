# Generated by Django 2.2.7 on 2019-12-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]
