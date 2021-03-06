# Generated by Django 3.1.2 on 2020-11-04 08:23

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zenatixTask', '0011_auto_20201104_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('grand_total', models.FloatField(blank=True, default=0, null=True)),
                ('products', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
