# Generated by Django 2.0.3 on 2018-04-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_article_youneed_know'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
    ]