# Generated by Django 3.2.7 on 2022-05-31 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0010_alter_productcomment_comment_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0009_alter_address_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveIntegerField()),
                ('created_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('delivery_status', models.CharField(choices=[('سفارش ثبت شده', 'سفارش ثبت شده'), ('در حال بسته بندی', 'در حال بسته بندی'), ('آماده ارسال', 'آماده ارسال'), ('فرستاده شده', 'فرستاده شده'), ('دریافت شده است', 'دریافت شده است')], default='سفارش ثبت شده', max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.address')),
                ('order_items', models.ManyToManyField(to='cart.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
