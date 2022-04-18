# Generated by Django 3.2.13 on 2022-04-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve_official', '0002_auto_20220416_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(blank=True, max_length=512, null=True, verbose_name='img')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('type', models.CharField(choices=[('GENERAL', 'GENERAL'), ('STORE', 'STORE')], default='GENERAL', max_length=64, verbose_name='type')),
                ('store_id', models.IntegerField(blank=True, null=True, verbose_name='store_id')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='time')),
            ],
            options={
                'db_table': 'NOTIFICATION',
            },
        ),
    ]
