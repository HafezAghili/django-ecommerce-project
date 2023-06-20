# Generated by Django 4.2 on 2023-06-18 17:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_product_expiration_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Ready to send', 'Ready to send'), ('Sent', 'Sent')], default='Submitted', max_length=50),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pages.order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration_at',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 21, 34, 38, 281147)),
        ),
    ]
