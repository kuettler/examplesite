# Generated by Django 2.0.3 on 2018-03-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(default='Empty', max_length=200),
            preserve_default=False,
        ),
    ]