# Generated by Django 3.0.3 on 2020-02-05 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/static/projects/img/'),
        ),
    ]