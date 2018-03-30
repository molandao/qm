# Generated by Django 2.0.3 on 2018-03-25 05:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='组织名称')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='org/%Y%m', verbose_name='封面图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '组织机构',
                'verbose_name': '组织机构',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='笔名')),
                ('mu_years', models.IntegerField(default=0, verbose_name='网龄')),
                ('writing_style', models.CharField(max_length=50, verbose_name='文章风格')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.ArticleOrg', verbose_name='所属组织')),
            ],
            options={
                'verbose_name_plural': '作者',
                'verbose_name': '作者',
            },
        ),
    ]