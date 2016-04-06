# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0002_auto_20160401_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='Inappropriate',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='avg_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='content_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='creation_date',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='edm_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='greads_review_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='index',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='long_desc',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='long_desc_html',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='not_helpful',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='resource_types',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='seller_thumb_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='spam',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='title',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='wrong_tags',
            field=models.IntegerField(default=0, null=True),
        ),
    ]