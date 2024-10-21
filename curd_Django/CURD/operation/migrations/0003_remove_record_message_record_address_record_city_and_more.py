# Generated by Django 5.1.2 on 2024-10-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_remove_record_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='message',
        ),
        migrations.AddField(
            model_name='record',
            name='address',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='city',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='country',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='province',
            field=models.CharField(default='None', max_length=100),
        ),
    ]