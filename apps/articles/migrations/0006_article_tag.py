# Generated by Django 2.0.3 on 2018-04-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='文章标签'),
        ),
    ]
