# Generated by Django 4.1.3 on 2022-11-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
