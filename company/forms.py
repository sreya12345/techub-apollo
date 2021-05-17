from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(label='Company Name', max_length=100)


class EstimateForm(forms.Form):
    environmental_score = forms.FloatField()
    social_score = forms.FloatField()
    governance_score = forms.FloatField()
