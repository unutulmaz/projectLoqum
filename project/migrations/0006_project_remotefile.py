# Generated by Django 2.2.6 on 2019-11-01 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20191101_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='remoteFile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.RemoteFile'),
            preserve_default=False,
        ),
    ]