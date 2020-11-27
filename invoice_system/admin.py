from django.contrib import admin
from .models import (
	Shitje, Fletpercjellja, Product,
	FaturaHyrese, Hyrje
)


class ShitjeInLine(admin.TabularInline):
	model = Shitje
	readonly_fields = ('totali',)
	can_delete = False

class HyrjeInline(admin.TabularInline):
	model = Hyrje
	readonly_fields = ('totali',)
	can_delete = False

class FletpercjelljaAdmin(admin.ModelAdmin):
	inlines = [
		ShitjeInLine,
	]

	list_display = ('fletpercjellja_id', 'fletpercjellja_data', 'fletpercjellja_verejtje','get_total')
	readonly_fields = ('get_total',)
	list_editable = ('fletpercjellja_data',)

class ShitjeAdmin(admin.ModelAdmin):
	list_display = ('product', 'fletpercjellja', 'shitje_quantity', 'shitje_price')
	readonly_fields = ('totali',)


class FaturaHyreseAdmin(admin.ModelAdmin):
	inlines = [
		HyrjeInline,
	]

	list_display = ('fathyrese_id', 'fathyrese_data', 'fathyrese_verejtje','get_total')
	readonly_fields = ('get_total',)
	list_editable = ('fathyrese_data',)

class HyrjeAdmin(admin.ModelAdmin):
	list_display = ('product', 'fathyrese', 'hyrje_quantity', 'hyrje_price')
	readonly_fields = ('totali',)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_id', 'product_name', 'product_desc', 'product_price', 'quantity')
	readonly_fields = ('quantity',)



admin.site.register(Fletpercjellja, FletpercjelljaAdmin)
admin.site.register(Shitje, ShitjeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(FaturaHyrese, FaturaHyreseAdmin)
admin.site.register(Hyrje, HyrjeAdmin)









