from django.contrib import admin

from app1.models import Book
admin.site.register(Book)

from app1.models import Person
admin.site.register(Person)

from app1.models import Myuser
admin.site.register(Myuser)

