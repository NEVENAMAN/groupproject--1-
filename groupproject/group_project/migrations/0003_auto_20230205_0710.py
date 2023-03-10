# Generated by Django 2.2.13 on 2023-02-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_project', '0002_auto_20230205_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='identity_number',
            field=models.IntegerField(default=1234567890, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]
