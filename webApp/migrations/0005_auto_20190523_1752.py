# Generated by Django 2.2.1 on 2019-05-23 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webApp', '0004_token_descriptoins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='descriptoins',
        ),
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]