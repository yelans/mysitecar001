# Generated by Django 2.1.4 on 2019-02-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_carrealtimetest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrealtimetest',
            name='Chargingstatus',
            field=models.CharField(choices=[('0', '停车充电'), ('1', '行驶充电'), ('2', '未充电'), ('3', '充电完成')], max_length=24, verbose_name='充电状态'),
        ),
        migrations.AlterField(
            model_name='carrealtimetest',
            name='DC_DC',
            field=models.CharField(choices=[('0', '工作'), ('1', '断开')], max_length=24, verbose_name='DC/DC状态'),
        ),
        migrations.AlterField(
            model_name='carrealtimetest',
            name='Statevehicle',
            field=models.CharField(choices=[('0', '启动'), ('1', '熄火'), ('2', '其他')], max_length=24, verbose_name='车辆状态'),
        ),
    ]