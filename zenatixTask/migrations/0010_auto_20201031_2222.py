# Generated by Django 3.1.2 on 2020-10-31 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zenatixTask', '0009_auto_20201031_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qauntity',
            new_name='quantity',
        ),
    ]
