# Generated by Django 5.1.2 on 2024-10-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_remove_record_message_record_address_record_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]