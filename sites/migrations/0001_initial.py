# Generated by Django 2.0.3 on 2018-03-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('value_a', models.IntegerField(default=0)),
                ('value_b', models.IntegerField(default=0)),
            ],
        ),
    ]
