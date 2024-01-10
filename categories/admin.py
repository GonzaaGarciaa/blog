from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published'] # Ponemos los campos que queremos que se muestren en el admin