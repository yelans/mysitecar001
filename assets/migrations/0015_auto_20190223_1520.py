# Generated by Django 2.1.4 on 2019-02-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_testwarn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testwarn',
            name='warnhigh',
            field=models.CharField(choices=[('01', '1级故障'), ('02', '2级故障'), ('03', '3级故障'), ('03', '正常'), ('FE', '异常')], max_length=24, verbose_name='最高报警等级'),
        ),
    ]