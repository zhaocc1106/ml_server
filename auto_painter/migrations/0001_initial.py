# Generated by Django 3.0.1 on 2020-01-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPainter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('begin_stroke', models.FloatField(max_length=500)),
                ('follow_stroke', models.FloatField(max_length=500)),
            ],
        ),
    ]
