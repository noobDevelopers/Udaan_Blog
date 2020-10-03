# Generated by Django 3.0.3 on 2020-04-01 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blogs', '0013_auto_20200401_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 23, 38, 353421, tzinfo=utc)),
        ),
    ]