# Generated by Django 2.0.3 on 2018-03-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='articles/%Y%m', verbose_name='封面图'),
        ),
    ]
