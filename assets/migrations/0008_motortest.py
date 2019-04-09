# Generated by Django 2.1.4 on 2019-02-12 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_motor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motortest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('torque', models.FloatField(max_length=48, verbose_name='电机转矩')),
                ('torquespeed', models.FloatField(max_length=48, verbose_name='电机转速')),
                ('torquecurrent', models.FloatField(max_length=48, verbose_name='电机母线电压')),
                ('torquemileage', models.FloatField(max_length=48, verbose_name='电机母线电流')),
                ('local_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('Carformtest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Carformtest', verbose_name='汽车名称')),
            ],
        ),
    ]