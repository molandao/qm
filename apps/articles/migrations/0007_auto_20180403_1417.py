# Generated by Django 2.0.3 on 2018-04-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content',
            field=models.TextField(null=True, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=100, verbose_name='文章标题'),
        ),
    ]
