from django.contrib import admin
from .models import Agent,Property,Image,Amenities,Post,postComments,Contact

# Register your models here.
admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(Amenities)
admin.site.register(Post)
admin.site.register(postComments) 
admin.site.register(Contact) 
