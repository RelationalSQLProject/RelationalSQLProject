from django.contrib import admin
from listings.models import Listing, Product, Bid

# Register your models here.
admin.site.register(Listing)
admin.site.register(Product)
admin.site.register(Bid)
