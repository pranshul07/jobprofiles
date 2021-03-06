# Generated by Django 2.0.6 on 2018-06-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('job_profile', models.CharField(max_length=250)),
                ('job_description', models.TextField(blank=True, default=None)),
                ('requirements', models.TextField(blank=True, default=None)),
                ('salary', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('experience', models.CharField(blank=True, default=None, max_length=250, null=True)),
            ],
        ),
    ]
