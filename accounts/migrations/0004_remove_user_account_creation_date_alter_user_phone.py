# Generated by Django 4.2.7 on 2023-12-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_creation_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
