# Generated by Django 2.1.5 on 2020-06-26 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userAuth',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='socialaccount.SocialAccount'),
        ),
    ]
