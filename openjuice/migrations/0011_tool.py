# Generated by Django 3.0.2 on 2020-02-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openjuice', '0010_auto_20200223_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('topics', models.ManyToManyField(to='openjuice.Topic')),
            ],
        ),
    ]