# Generated by Django 3.1.7 on 2023-12-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]