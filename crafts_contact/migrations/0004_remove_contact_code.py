# Generated by Django 3.2.4 on 2024-04-01 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_contact', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='code',
        ),
    ]
