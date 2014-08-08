from django import forms
from apps.core.models import *


class ChallengeForm(forms.ModelForm):
	"""
	Fromulario para crear torneos
	"""
	class Meta:
		model = Torneo
