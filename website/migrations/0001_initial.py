# Generated by Django 5.1.5 on 2025-05-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='WHO WE ARE', max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='WORKHORSE', max_length=100)),
                ('media', models.FileField(upload_to='home_media/')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='crew/')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
