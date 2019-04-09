# Generated by Django 2.1.4 on 2019-04-01 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_zjgzm'),
    ]

    operations = [
        migrations.CreateModel(
            name='morepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statevehicle', models.CharField(choices=[('01', '启动'), ('02', '熄火'), ('03', '其他'), ('FE', '异常')], max_length=24, verbose_name='车辆状态')),
                ('speed', models.FloatField(max_length=48, verbose_name='车速')),
                ('serialnum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.testcarform', verbose_name='内部编号')),
            ],
        ),
        migrations.CreateModel(
            name='realpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField(max_length=48, verbose_name='车速')),
                ('serialnum', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.testcarform', verbose_name='内部编号')),
            ],
        ),
    ]
