# Generated by Django 2.1.3 on 2018-11-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_request_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Store'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='rest',
            unique_together={('store', 'item')},
        ),
    ]
