# Generated by Django 2.2.6 on 2019-10-22 12:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueKey', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RemoteFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fileType', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=200000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('zipFile', models.FileField(upload_to='')),
                ('remoteFiles', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.RemoteFile')),
            ],
        ),
    ]
