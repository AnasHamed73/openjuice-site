# Generated by Django 3.0.2 on 2020-02-01 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openjuice', '0002_domain_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='topics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='openjuice.Topic'),
        ),
    ]