# Generated by Django 4.2.13 on 2024-07-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0005_alter_tweet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]