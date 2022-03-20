# Generated by Django 4.0.2 on 2022-03-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_alter_notification_notification_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_id',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_type',
        ),
        migrations.AddField(
            model_name='notification',
            name='content',
            field=models.TextField(default=False),
        ),
    ]
