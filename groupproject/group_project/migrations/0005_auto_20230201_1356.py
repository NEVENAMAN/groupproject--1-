# Generated by Django 2.2.4 on 2023-02-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_project', '0004_auto_20230201_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='user_level',
            field=models.ManyToManyField(related_name='members', to='group_project.userLevel'),
        ),
    ]
