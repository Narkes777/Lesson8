# Generated by Django 5.0.1 on 2024-01-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_ad_is_active_ad_status_alter_ad_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.CharField(choices=[(None, 'Выберите статус рекламы'), ('s', 'Продано'), ('a', 'Активна'), ('c', 'Отменена')], default='a', max_length=1),
        ),
    ]
