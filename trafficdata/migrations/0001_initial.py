# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KeyWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trafficdata.City')),
                ('key_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trafficdata.KeyWords')),
            ],
        ),
        migrations.CreateModel(
            name='QueryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.CharField(max_length=200, null=True)),
                ('tweet_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('traffic_info', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trafficdata.Query')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_Twitter_id', models.CharField(max_length=50, null=True)),
                ('screen_name', models.CharField(max_length=50, null=True)),
                ('followers_count', models.IntegerField(null=True)),
                ('friends_count', models.IntegerField(null=True)),
                ('time_zone', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tweets',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trafficdata.User'),
        ),
        migrations.AddField(
            model_name='query',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trafficdata.QueryType'),
        ),
        migrations.AlterUniqueTogether(
            name='query',
            unique_together=set([('query', 'city', 'key_word')]),
        ),
    ]
