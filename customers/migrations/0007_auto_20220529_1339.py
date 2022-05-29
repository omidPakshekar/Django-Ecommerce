# Generated by Django 3.2.7 on 2022-05-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_discountcode_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='address_text',
            field=models.CharField(default='', max_length=1200),
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]
