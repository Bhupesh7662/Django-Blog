# Generated by Django 3.0.6 on 2020-06-04 08:45

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('comment_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150)),
                ('short_desc', models.CharField(max_length=150)),
                ('long_desc', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('main_image', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('post_status', models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], max_length=150)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_slug', models.SlugField(editable=False, max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]
