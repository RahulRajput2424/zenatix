# Generated by Django 3.1.2 on 2020-10-31 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zenatixTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('quantity', models.IntegerField(unique=True)),
                ('unit', models.IntegerField(choices=[(1, 'kg')], default=None)),
                ('price', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
