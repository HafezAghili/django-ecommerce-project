from django import forms

class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
