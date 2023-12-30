# Generated by Django 5.0 on 2023-12-27 08:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=10)),
                ('reg_no', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Phone number must be at least 10 characters.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Phone number must be at most 10 characters.')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]