# Generated by Django 3.1.5 on 2021-01-27 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('location', models.TextField()),
                ('agenda', models.TextField()),
            ],
            options={
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=255)),
                ('resourceurl', models.URLField()),
                ('dateentered', models.DateField()),
                ('description', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutestext', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.meeting')),
            ],
            options={
                'db_table': 'meetingminutes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('eventdate', models.DateField()),
                ('eventtime', models.TimeField()),
                ('description', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
