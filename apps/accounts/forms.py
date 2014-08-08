from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from apps.core.models import Friki
#from apps.accounts.models import *



class FrikiForm(forms.ModelForm):
	"""
	Fromularios para registro de usuario
	"""

	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = Friki
		fields = ('alias', 'email')

	def clean_password2(self):
	# verifica si los password ingresados son identicos
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
    	# Almacena el password en un hash
		user = super(forms.ModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


class FrikiChangeForm(forms.ModelForm):
    """
    Formularios para modificar un usuario (No funciona aun)
    """

    #password = ReadOnlyPasswordHashField()
    location = forms.CharField(max_length = 50,help_text="Texto Ayuda", widget = forms.TextInput(attrs={'placeholder':'Enter your current location','class':'mi-clase'}))
    #alias = forms.CharField(max_length = 50, help_text="Ayuda", widget = forms.TextInput(attrs={'placeholder':'Enter your current location','class':''}))

    class Meta:
        model = Friki
        #fields = ('email', 'password', 'alias', 'is_active', 'is_staff')
        fields = ('email', 'password', 'alias')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
