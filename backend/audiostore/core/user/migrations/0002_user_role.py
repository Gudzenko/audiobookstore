# Generated by Django 4.2.1 on 2023-08-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SUPER_ADMIN', 'superAdmin'), ('ADMIN', 'admin'), ('USER', 'user')], default='SUPER_ADMIN', max_length=100, verbose_name='role'),
        ),
    ]
