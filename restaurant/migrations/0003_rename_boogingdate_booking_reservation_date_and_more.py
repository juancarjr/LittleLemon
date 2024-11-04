# Generated by Django 5.1.2 on 2024-11-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='boogingDate',
            new_name='reservation_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]