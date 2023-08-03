from app1.models import Book
from django import forms
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'


from app1.models import Person
from django import forms
class personform(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'

