# Generated by Django 4.2.13 on 2024-11-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0007_rename_photo_tweet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
