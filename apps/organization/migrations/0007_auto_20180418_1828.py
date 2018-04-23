# Generated by Django 2.0.3 on 2018-04-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_author_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleorg',
            name='category',
            field=models.CharField(choices=[('zzjg', '组织机构'), ('gx', '高校'), ('gr', '个人')], default='gr', max_length=20, verbose_name='组织类别'),
        ),
    ]
