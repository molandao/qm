# Generated by Django 2.0.3 on 2018-04-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_is_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(default='', upload_to='articles/%Y%m', verbose_name='封面图'),
        ),
    ]