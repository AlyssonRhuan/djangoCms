# Generated by Django 3.0.8 on 2020-07-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200701_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_pic',
            field=models.ImageField(upload_to='polls/static/assets/homepage/'),
        ),
    ]
