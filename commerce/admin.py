from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from commerce.models import unit,  Address,  ProductImage, City, Category, Vendor, Merchant, \
    Label


class InlineProductImage(admin.TabularInline):
    model = ProductImage

class HouseAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'room', 'description', 'price',)
    list_filter = ('category', 'label', 'merchant', 'vendor')
    search_fields = ('name', 'location', 'description', 'cost', 'price', 'vendor', 'merchant__name')

admin.site.register(unit, HouseAdmin)
admin.site.register(Address)
#admin.site.register(unit_image)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)
admin.site.register(Label)
