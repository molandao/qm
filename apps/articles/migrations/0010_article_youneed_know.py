# Generated by Django 2.0.3 on 2018-04-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='youneed_know',
            field=models.CharField(default='', max_length=300, verbose_name='自述'),
        ),
    ]
