# Generated by Django 5.0.1 on 2024-01-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_item_item_type_item_owner_item_placement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='placement',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
