# Generated by Django 3.0.3 on 2020-02-14 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=24)),
                ('vicinity', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('google_place_id', models.CharField(max_length=64)),
                ('geometry', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=32)),
                ('rating', models.FloatField()),
                ('review_text', models.TextField()),
                ('review_time', models.DateTimeField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('user_ratings_total', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hotel')),
            ],
        ),
    ]
