# Generated by Django 2.0.3 on 2018-04-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_article_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='散文', max_length=20, verbose_name='文章类别'),
        ),
    ]
