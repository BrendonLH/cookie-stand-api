# Generated by Django 4.1 on 2022-09-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cookie',
            name='hourly_sales',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='cookie',
            name='location',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='cookie',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cookie',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]