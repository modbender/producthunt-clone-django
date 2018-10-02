from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('image','icon','title','slug','product_date','modified_date','votes','desc','url','hunter')
        }),
    )
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('modified_date',)
    search_fields = ['title']
admin.site.register(Product, ProductAdmin)
