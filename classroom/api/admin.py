from django.contrib import admin

from api.models import Message,Contact
from api.models import Chat

# Register your models here.
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Contact)