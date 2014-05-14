from django.contrib import admin

# Register your models here.
from pizza.models import Pizza, Topping, ToppingUsage

class ToppingUsageInline(admin.StackedInline):
    model = ToppingUsage
    extra = 1

class PizzaAdmin(admin.ModelAdmin):
    inlines = [ToppingUsageInline,]

class ToppingAdmin(admin.ModelAdmin):
    inlines = [ToppingUsageInline,]

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
