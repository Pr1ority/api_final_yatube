# Generated by Django 3.2.15 on 2024-07-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20240701_1946'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower_following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following'),
        ),
    ]
