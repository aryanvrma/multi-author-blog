# Generated by Django 3.0 on 2021-07-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210712_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]