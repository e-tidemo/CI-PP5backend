# Generated by Django 3.2.4 on 2024-04-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_panel', '0003_auto_20240402_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='panel',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]