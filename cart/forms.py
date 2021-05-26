from django import forms

class CartAddProductForm(forms.Form):

    quantity = forms.ChoiceField(
        choices=((str(num), str(num)) for num in range(1, 11))
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )