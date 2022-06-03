import csv
import datetime
from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']

# Register your models here.
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['product.name', 'quantity']

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    print(opts)
    response = HttpResponse(content_type='text/csv')
    # we use this line code to indicate this HttpResponse has attachment file
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many ]
    # write the header raw
    writer.writerow([field.verbose_name for field in fields])
    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')

            data_row.append(unicode(value, "utf-8"))
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'export_to_csv'

def order_detail(obj):
    return mark_safe('<a href="{}"> Views </a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])
    ))

order_detail.description = 'Testing form output'
order_detail.allow_tags = True

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time', 'total_price', 'address', order_detail]
    # inlines = [OrderItemInline]
    actions = [export_to_csv]
    order_detail.allow_tags = True


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
