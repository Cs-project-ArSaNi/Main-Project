# Generated by Django 3.2.2 on 2022-02-04 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_checkout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='Phone',
            new_name='phone',
        ),
    ]