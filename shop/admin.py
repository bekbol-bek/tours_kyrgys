from django.contrib import admin
from .models import Product, TourCategory, Tour, EcosystemCategory, Ecosystem

admin.site.register(Product)


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')


@admin.register(EcosystemCategory)
class EcosystemCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

@admin.register(Ecosystem)
class EcosystemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'photo')

