from django.contrib import admin
from .models import Movies, Customer

# Register your models here.
# name of class should be name of model + admin
class MoviesAdmin(admin.ModelAdmin):
    # sequence in which you want to see the fields
    fields = ['release_year', 'title', 'length']

    # add a search field
    search_fields = ['title', 'length']

    # add filter
    list_filter = ['release_year', 'title', 'length']
    
    # how to display the all objects
    list_display = ['title', 'release_year', 'length']

    # add edit to list
    # remember that only the fields in list_display can be edited others can be edited by clicking on the object and going to detail view page
    list_editable = ['length']

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Customer)