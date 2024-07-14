# Generated by Django 4.2.8 on 2024-07-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file_path', models.FileField(upload_to='audio_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors_photos/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('series', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('narrator', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('illustration', models.ImageField(blank=True, null=True, upload_to='book_illustrations/')),
                ('audio_files', models.ManyToManyField(blank=True, to='main.audio')),
                ('authors', models.ManyToManyField(blank=True, to='main.author')),
                ('genres', models.ManyToManyField(blank=True, to='main.genre')),
            ],
        ),
    ]