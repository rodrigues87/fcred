# Generated by Django 3.0.8 on 2020-09-12 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicacao', '0005_indicacao_nome_indicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicacao',
            name='year_in_school',
            field=models.CharField(choices=[('EA', 'Em andamento'), ('FC', 'Fechado'), ('EF', 'Efetivado'), ('RC', 'Recusado')], default='EA', max_length=2),
        ),
        migrations.AlterField(
            model_name='indicacao',
            name='autorizado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicacao',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='indicacao',
            name='efetivada',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]