from django.contrib import admin

# Register your models here.

from .models import Person, Action, Automatable

admin.site.register(Person)
admin.site.register(Action)
admin.site.register(Automatable)