# Generated by Django 3.2.13 on 2022-05-27 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
