# Generated by Django 2.2.13 on 2023-02-05 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group_project', '0003_auto_20230205_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_recieve', to='group_project.customers'),
        ),
    ]
