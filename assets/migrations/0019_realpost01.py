# Generated by Django 2.1.4 on 2019-04-01 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_morepost_realpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='realpost01',
            fields=[
                ('serialnum', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='assets.testcarform', verbose_name='内部编号')),
                ('speed', models.FloatField(max_length=48, verbose_name='车速')),
                ('Statevehicle', models.CharField(choices=[('01', '启动'), ('02', '熄火'), ('03', '其他'), ('FE', '异常')], max_length=24, verbose_name='车辆状态')),
            ],
        ),
    ]
