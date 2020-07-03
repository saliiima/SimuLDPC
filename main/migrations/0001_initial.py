# Generated by Django 2.1.5 on 2020-07-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_type', models.CharField(max_length=200)),
                ('channel_summary', models.CharField(max_length=200)),
                ('channel_img', models.ImageField(upload_to='figs')),
                ('channel_slug', models.SlugField(max_length=40)),
            ],
        ),
    ]
