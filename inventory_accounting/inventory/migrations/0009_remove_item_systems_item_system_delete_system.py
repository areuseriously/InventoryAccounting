# Generated by Django 5.0.1 on 2024-01-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_remove_item_system_system_item_systems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='systems',
        ),
        migrations.AddField(
            model_name='item',
            name='system',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.DeleteModel(
            name='System',
        ),
    ]
