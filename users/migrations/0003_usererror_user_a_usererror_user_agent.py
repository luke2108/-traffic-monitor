# Generated by Django 5.0 on 2023-12-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usererror_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='usererror',
            name='user_a',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='usererror',
            name='user_agent',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
