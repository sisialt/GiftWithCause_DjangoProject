# Generated by Django 4.2.16 on 2024-12-09 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_gift_created_at'),
        ('gift_searches', '0002_giftsearch_created_at'),
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='to_gift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gifts.gift'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_gift_search',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gift_searches.giftsearch'),
        ),
    ]
