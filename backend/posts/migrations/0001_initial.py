# Generated by Django 5.0.6 on 2024-08-04 18:46

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('link', models.URLField()),
                ('date', models.DateTimeField()),
                ('page_title', models.CharField(blank=True, max_length=200, null=True)),
                ('page_desc', models.TextField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='')),
                ('colour', colorfield.fields.ColorField(default='#EEEEEE', image_field=None, max_length=25, samples=None)),
                ('contrast_colour', colorfield.fields.ColorField(default='#4E4E4E', image_field=None, max_length=25, samples=None)),
                ('use_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='posts.tag'),
        ),
    ]
