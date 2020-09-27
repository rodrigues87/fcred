# Generated by Django 3.0.8 on 2020-09-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_expiracao', models.DateTimeField()),
                ('codigo_verificador', models.CharField(max_length=30)),
                ('codigo_verificador_tentado', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Conta',
            },
        ),
    ]
