# Generated by Django 3.0.8 on 2020-10-29 16:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Termos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.TextField(blank=True, max_length=250, validators=[django.core.validators.MaxLengthValidator(250)])),
            ],
        ),
        migrations.CreateModel(
            name='Aceite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aceite', models.BooleanField(default=False)),
                ('termo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='termos.Termos')),
            ],
        ),
    ]