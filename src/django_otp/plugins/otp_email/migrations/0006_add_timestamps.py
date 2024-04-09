# Generated by Django 4.2.7 on 2024-04-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('otp_email', '0005_emaildevice_last_generated_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaildevice',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                help_text='The date and time when this device was initially created in the system.',
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='emaildevice',
            name='last_used_at',
            field=models.DateTimeField(
                blank=True,
                help_text='The most recent date and time this device was used.',
                null=True,
            ),
        ),
    ]