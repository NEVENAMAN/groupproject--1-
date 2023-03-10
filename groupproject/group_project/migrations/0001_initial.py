# Generated by Django 2.2.13 on 2023-02-04 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('identity_number', models.IntegerField(unique=True)),
                ('mobile_num', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('skill', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('mobile_num', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
                ('identity_image', models.FileField(blank=True, default='', max_length=250, null=True, upload_to='identity_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='userLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('identity_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=255)),
                ('telphone_number', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('service_desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to='group_project.members')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_context', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('send_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_send', to='group_project.members')),
                ('send_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_recieve', to='group_project.members')),
            ],
        ),
        migrations.AddField(
            model_name='members',
            name='user_level',
            field=models.ManyToManyField(related_name='members', to='group_project.userLevel'),
        ),
    ]
