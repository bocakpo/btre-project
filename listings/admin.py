from django.contrib import admin
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'listing_date', 'realtor') #hace que se muestren los campos en http://127.0.0.1:8000/admin/listings/listing/
    list_display_links = ('id', 'title') #hace que esos campos sean links a la publicacion
    list_filter = ('realtor',) #crea una vista de filtro
    list_editable = ('is_published',) #hace que los campos sean editables
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #crea una busqueda
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)