# Generated by Django 4.2.16 on 2024-11-28 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gifts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='gifts.gift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]