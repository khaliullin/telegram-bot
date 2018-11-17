from django.contrib import admin

from shop.models import Category, Item, Client, Request, Store, Rest

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Client)
admin.site.register(Request)
admin.site.register(Rest)
