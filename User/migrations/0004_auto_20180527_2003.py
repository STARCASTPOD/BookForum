# Generated by Django 2.0.5 on 2018-05-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User', '0003_auto_20180527_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
    ]