# Generated by Django 5.0.2 on 2024-06-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginScreens', '0002_alter_scholar_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='Password',
            field=models.CharField(max_length=50),
        ),
    ]