# Generated by Django 4.2.16 on 2024-12-08 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
