# Generated by Django 2.0.3 on 2018-03-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180331_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
